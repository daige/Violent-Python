#!/usr/bin/env python
#encoding=utf-8
#匿名ftp扫描器

import ftplib
import optparse
from threading import *

maxConnections = 100

connection_lock = BoundedSemaphore(value = maxConnections)

def anonLogin(hostname,release):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('ftp','ftp')
        print '[*]'+ str(hostname)
        ftp.quit()
        return True
    except Exception,e:
        return False
    finally:
        if release:
            connection_lock.release()


def main():
    parser = optparse.OptionParser('usage %prog -H <target host>')
    parser.add_option('-H',dest='hostfile',type='string',help='specify host file')

    (options,args) = parser.parse_args()

    hostfile = options.hostfile

    if hostfile == None:
        print parser.usage
        exit(0)
    
    fn = open(hostfile,'r')
    for host in fn.readlines():
        host = host.strip('\n')
        
        connection_lock.acquire()
        t = Thread(target=anonLogin,args=(host,True))
        child = t.start()


if __name__ == '__main__':
    main()
    
