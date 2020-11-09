# -*- coding: utf-8 -*-
import sys,os,time
import hashlib
os.system("clear")

UseMd5 = False
result = ""
UseSha1 = False

def banner():
	print("██   ██  █████  ███████ ██   ██  ██████ ██████   █████   ██████ ██   ██ ")
	print("██   ██ ██   ██ ██      ██   ██ ██      ██   ██ ██   ██ ██      ██  ██  ")
	print("███████ ███████ ███████ ███████ ██      ██████  ███████ ██      █████   ")
	print("██   ██ ██   ██      ██ ██   ██ ██      ██   ██ ██   ██ ██      ██  ██  ")
	print("██   ██ ██   ██ ███████ ██   ██  ██████ ██   ██ ██   ██  ██████ ██   ██ ")
	print("------------------------------------------------------------------------")
	print("Simple hash Brute-Force")
	print("------------------------------------------------------------------------")
	print("Github: https://github.com/diego-tella/Hash-Crack")
	print("------------------------------------------------------------------------")


def ErroArg():
    print("- Put the arguments like below")
    print("- python3 script.py HASH wordlist.txt")
    print("- python3 script.py MD5 rockyou.txt\n")
    print("- Supported arguments: ")
    print("● MD5 - Brute-Force in hashs MD5. Use: python3 script.py MD5 file.txt")
    print("● SHA1 - Brute-Force in hashs SHA1. Use: python3 script.py SHA1 file.txt")


def Comeca():
    achou = False
    str2hash = input("What is the hash? ") #inserindo a hash aqui
    wordlist = sys.argv[2] #declarando a variável do arquivo de wordlist
    file = open(wordlist, encoding = "utf8", errors='replace') #abrindo a wordlist e lendo
    print("\n["+time.strftime("%H:%M:%S")+"] Starting brute-force\n")
    for i in file.readlines(): #i vira todas as linhas
        i = i.rstrip("\n")
        if UseMd5:
            result = hashlib.md5(i.encode()) #result vai receber i (wordlist) encodado
        elif UseSha1:
            result = hashlib.sha1(i.encode())

        hash2 = result.hexdigest() #passa a hash pra variável hash2
        #print(hash2)
        if hash2 == str2hash: #faz a comparação se a hash passada pelo usuário é a hash do arquivo
            print("\n["+time.strftime("%H:%M:%S")+"] Hash Cracked!\n")
            print("\n["+time.strftime("%H:%M:%S")+"] End of brute-force \n")
            achou = True
            print(str2hash+":"+i) #hashAchada:senhaLimpa
            quit()
    
    if achou == False:
        print("\n["+time.strftime("%H:%M:%S")+"] End of brute-force\n")
        print("The hash was not found ")

banner()

if len(sys.argv) != 3: #script.py é o argumento 0!
    ErroArg()
else:
    if sys.argv[1] == "md5" or sys.argv[1] == "MD5":
        UseMd5 = True
        Comeca()
    elif sys.argv[1] == "sha1" or sys.argv[1] == "SHA1":
        UseSha1 = True
        Comeca()
        
