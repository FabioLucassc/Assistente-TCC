import os
from os import path

caminho = path.join(path.expanduser("~"))

diretorio = ""

while (True):
    palavra = input('Diretorio inicial: ')
    if (palavra == "D:"):
        palavra = ""
        diretorio = "D:\\"
        print(os.listdir(diretorio))
        while (True):
            try:
                palavra = input("Qual diretorio ?\n"+str(os.listdir(diretorio))+"\n")
                diretorio += "\\" + palavra
            except:
                print("diretorio não encontrado")
                print(diretorio)

    else:
        diretorio += "\\" + palavra
        print(os.listdir(diretorio))
