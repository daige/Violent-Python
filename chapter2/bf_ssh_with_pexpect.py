#!/usr/bin/env python
#encoding=utf-8
#用pexpect爆破ssh by daige

import pexpect

PROMPT =['# ','>>> ','> ','\$ ']

def send_command(child,cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def conn_ssh(user,host,passwd):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user +'@' + host
   
    child = pexpect.spawn(connStr)
    
    ret = child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword:'])
    if ret == 0:
        print '[-] Error Connecting'
        return 
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
        if ret == 0:
            print '[-] Error Connecting'
            return
    child.sendline(passwd)
    child.expect(PROMPT)
    return child

def main():
    host = '127.0.0.1'
    user = 'root'
    password = '******'

    child = conn_ssh(user,host,password)
    send_command(child,'uname -v')

if __name__ == '__main__':
    main()
