#!/usr/bin/env python
#encoding=utf-8
#在ftp服务器上搜索web网页入口

import ftplib

def retrunDefault(ftp):
    try:
        dirList = ftp.nlst()
        print dirList
    except:
        dirList=[]
        print "[-] can't list the directory contents."
        print "[-] Skipping To Next Target"
        return
    
    for filename in dirList():
        fn = filename.lower()
        if '.php' in fn or '.html' in fn or '.asp' in fn:
            print '[+] Found default page:' + filename
            retList.append(filename)

    return retList

host = '127.0.0.1'
user = 'ftp'
password='ftp'
ftp = ftplib.FTP(host)
ftp.login(user,password)
retrunDefault(ftp)
