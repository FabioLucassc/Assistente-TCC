import os
from os import path

caminho = path.join(path.expanduser("~"))
# print(str(os.listdir("D:\\temp\\teste")))

diretorio = ""
diretorio_anterior = ""

while (True):

    palavra = input('Diretorio inicial: ')

    if (palavra == "D:"):

        palavra = ""
        diretorio = "D:\\"
        diretorio_anterior = diretorio

        while (True):

            diretorio_anterior = diretorio

            try:

                palavra = input("Qual diretorio ?\n"+str(os.listdir(diretorio))+"\n")
                diretorio += "\\" + palavra
                os.listdir(diretorio)

            except:

                print("diretorio não encontrado")
                diretorio = diretorio_anterior

    elif (palavra == "C:"):

        palavra = ""
        diretorio = "C:\\"
        diretorio_anterior = diretorio

        while (True):

            diretorio_anterior = diretorio

            try:

                palavra = input("Qual diretorio ?\n" + str(os.listdir(diretorio)) + "\n")
                diretorio += "\\" + palavra
                os.listdir(diretorio)

            except:

                print("diretorio não encontrado")
                diretorio = diretorio_anterior
    else:
        print("Disco não encontrado")