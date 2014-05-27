#!/usr/bin/env python
#encoding=utf-8
# 利用nmap进行端口扫描

import nmap
import socket
import optparse

def nmapScan(host,port):
    host = socket.gethostbyname(host)
    nmScan = nmap.PortScanner()
    nmScan.scan(host,port)
    state = nmScan[host]['tcp'][int(port)]['state']
    print " [*] " + host + " tcp/"+port +' '+state


def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H',dest ='host',type='string',help='specify target host')
    parser.add_option('-p',dest ='port',type='string',help='specify target port[s])')
    (options,args) = parser.parse_args()

    host  = options.host
    ports = str(options.port).split(',')

    if( host == None) | (ports[0] == None):
        print parser.usage
        exit(0)

    for port in ports:
        nmapScan(host,port)

if __name__ == '__main__':
    main()

