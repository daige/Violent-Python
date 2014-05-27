#!/usr/bin/env python
#encoding=utf-8
#TCP端口扫描器 by daige

import socket
import threading
import optparse

screenLock = threading.Semaphore(value=1)
def main():
    parser = optparse.OptionParser("usage: %prog -H  <target host> -p <target port>")
    parser.add_option('-H',dest='host',type='string',help='specify target host')
    parser.add_option('-p',dest='port',type='string',help='specify target port')
    (options,args)=parser.parse_args()

    host = options.host
    ports = str(options.port).split(',')

    if( host == None)|(ports == None):
        print parser.usage
        exit(0)
    portScan(host,ports)


def connScan(host,port):
    try:
        connSocket =socket.socket(AF_INET,SOCK_STREAM)
        connSocket =socket.connect(host,port)
        connSocket.send("daige's test\r\n")
        results = connSocket.recv(1000)
        
        screenLock.acquire()
        print '[+]%d/tcp open' % port
        print '[+]' + str(results)

        connSocket.close()
    except:
        print '[-]%d/tcp closed ' % port
    finally:
        screenLock.release()


def portScan(host,ports):
    try:
        ip =socket.gethostbyname(host)
    except:
        print "[-]Cannot resolve '%s': unknown host" %host
        return
    try:
        name =socket.gethostbyaddr(ip)
        print '\n[+]Scan Results for:' + name[0]
    except:
        print '\n[+]Scan Results for:' + ip
    socket.setdefaulttimeout(1)
    for port in ports:
        print 'Scanning  port:' + port
        t = threading.Thread(target=connScan,args=(host,int(port)))
        t.start()


if __name__ == '__main__':
    main()
