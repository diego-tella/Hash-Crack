# -*- coding: utf-8 -*-
#https://www.geeksforgeeks.org/md5-hash-python/
import sys,os
import hashlib
os.system("clear")

def banner():
	print("██   ██  █████  ███████ ██   ██  ██████ ██████   █████   ██████ ██   ██ ")
	print("██   ██ ██   ██ ██      ██   ██ ██      ██   ██ ██   ██ ██      ██  ██  ")
	print("███████ ███████ ███████ ███████ ██      ██████  ███████ ██      █████   ")
	print("██   ██ ██   ██      ██ ██   ██ ██      ██   ██ ██   ██ ██      ██  ██  ")
	print("██   ██ ██   ██ ███████ ██   ██  ██████ ██   ██ ██   ██  ██████ ██   ██ ")

def ErroArg():
    print("Coloque os argumentos!")
    print("python3 script.py md5 wordlist.txt")


def ComecaMD5():
    str2hash = input("Qual a hash? ") #inserindo a hash aqui
    wordlist = sys.argv[2] #declarando a variável do arquivo de wordlist
    file = open(wordlist, encoding = "utf8", errors='replace') #abrindo a wordlist e lendo
    for i in file.readlines(): #i vira todas as linhas
        result = hashlib.md5(i.encode()) #result vai receber i (wordlist) encodado

        hash2 = result.hexdigest() #passa a hash pra variável hash2
        if hash2 == str2hash: #faz a comparação se a hash passada pelo usuário é a hash do arquivo
        	print("Hash de " + str2hash + " é: " + i) #se for, imprimi isso
        	print(str2hash+":"+i) #hashAchada:senhaLimpa


banner()

if len(sys.argv) != 3: #script.py é o argumento 0!
    ErroArg()
else:
    if sys.argv[1] == "md5" or sys.argv[1] == "MD5":
        ComecaMD5()
    else:
        print("Esse seria o sha1")

