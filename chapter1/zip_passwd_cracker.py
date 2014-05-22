#!/usr/bin/env python
#ecoding=utf-8
#zip文件密码破解

import zipfile
import optparse
import sys
from threading import Thread

def extractFill(zFile,password):
    try:
        zFile.extractall(pwd = password)
        print '[+] Found password: '+ password 
    except:
        pass

def main():
    usage = "usage: %prog  -f <zipfile> -d <dict>"
    parser = optparse.OptionParser(usage)
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dict file')
    (options,args) = parser.parse_args()
  
    if (options.zname == None) |(options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFill,args=(zFile,password))
        t.start()

if __name__ == '__main__':
    main()

