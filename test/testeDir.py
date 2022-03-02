import os
import string
import subprocess
from os import path

alfabeto = list(string.ascii_lowercase)
caminho = path.join(path.expanduser("~"))
# print(str(os.listdir("D:\\temp\\teste")))

diretorio = ""
diretorio_anterior = ""

# while (True):
#
#     palavra = input('Diretorio inicial: ')
#
#     if (palavra == "D:"):
#
#         palavra = ""
#         diretorio = "D:\\"
#         diretorio_anterior = diretorio
#
#         while (True):
#
#             diretorio_anterior = diretorio
#
#             try:
#
#                 palavra = input("Qual diretorio ?\n"+str(os.listdir(diretorio))+"\n")
#                 diretorio += "\\" + palavra
#                 os.listdir(diretorio)
#
#             except:
#
#                 print("diretorio não encontrado")
#                 diretorio = diretorio_anterior
#
#     elif (palavra == "C:"):
#
#         palavra = ""
#         diretorio = "C:\\"
#         diretorio_anterior = diretorio
#
#         while (True):
#
#             diretorio_anterior = diretorio
#
#             try:
#
#                 palavra = input("Qual diretorio ?\n" + str(os.listdir(diretorio)) + "\n")
#                 diretorio += "\\" + palavra
#                 os.listdir(diretorio)
#
#             except:
#
#                 print("diretorio não encontrado")
#                 diretorio = diretorio_anterior
#     elif (palavra in a):
#         print("Teste")
#     else:
#         print("Disco não encontrado")

while (True):

    palavra = input('Qual disco inicial: ')

    if (palavra.lower() in alfabeto):
        # palavra = ""
        # diretorio = "C:\\"
        diretorio = palavra.upper()+":\\"
        diretorio_anterior = diretorio

        while (True):

            diretorio_anterior = diretorio


            try:

                palavra = input("Qual diretorio ?\n" + str(os.listdir(diretorio)) + "\n")
                diretorio += "\\" + palavra
                # if ((".txt" or ".lnk" or ".exe" or ".docx" or ".xls") in diretorio):
                if (".lnk" in diretorio):
                    # subprocess.Popen(f'notepad.exe "{diretorio}"')
                    os.startfile(diretorio)
                else:
                    os.listdir(diretorio)

            except:
                print("diretorio não encontrado")
                if (diretorio == palavra.upper() + ":\\"):
                    print("Por favor selecione um disco válido!")
                    break
                diretorio = diretorio_anterior

    else:
        print("Por favor selecione um disco válido!")