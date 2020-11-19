# -*- coding: utf-8 -*-
import sys,os,time,hashlib
os.system("clear")

UseMd5 = False
result = ""
UseSha1 = False

def banner():
    print('''
██╗  ██╗ █████╗ ███████╗██╗  ██╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
███████║███████║███████╗███████║    ██║     ██████╔╝███████║██║     █████╔╝ 
██╔══██║██╔══██║╚════██║██╔══██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██║  ██║██║  ██║███████║██║  ██║    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝        
----------------------------------------------------------------------------
Simple hash Brute-Force  
----------------------------------------------------------------------------
Github: https://github.com/diego-tella/Hash-Crack       
----------------------------------------------------------------------------                                                          
    ''')


def ErroArg():
    print("- Put the arguments like below")
    print("- python3 script.py HASH wordlist.txt")
    print("- python3 script.py MD5 rockyou.txt\n")
    print("- Supported arguments: ")
    print("● MD5 - Brute-Force in hashs MD5. Use: python3 script.py MD5 file.txt")
    print("● SHA1 - Brute-Force in hashs SHA1. Use: python3 script.py SHA1 file.txt")


def Comeca():
    achou = False
    str2hash = input("What is the hash? ")
    wordlist = sys.argv[2] 
    file = open(wordlist, encoding = "utf8", errors='replace') 
    print("\n["+time.strftime("%H:%M:%S")+"] Starting brute-force\n")
    for i in file.readlines(): 
        i = i.rstrip("\n")
        if UseMd5:
            result = hashlib.md5(i.encode()) 
        elif UseSha1:
            result = hashlib.sha1(i.encode())

        hash2 = result.hexdigest() 
        if hash2 == str2hash: 
            print("\n["+time.strftime("%H:%M:%S")+"] Hash Cracked!\n")
            print("\n["+time.strftime("%H:%M:%S")+"] End of brute-force \n")
            achou = True
            print(str2hash+":"+i) 
            quit()
    
    if achou == False:
        print("\n["+time.strftime("%H:%M:%S")+"] End of brute-force\n")
        print("The hash was not found ")

banner()

if len(sys.argv) != 3: 
    ErroArg()
else:
    if sys.argv[1] == "md5" or sys.argv[1] == "MD5":
        UseMd5 = True
        Comeca()
    elif sys.argv[1] == "sha1" or sys.argv[1] == "SHA1":
        UseSha1 = True
        Comeca()
    else:
        print("Invalid argument. Use only MD5 or SHA1.")
