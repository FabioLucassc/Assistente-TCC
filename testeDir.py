import os
import string
import subprocess
from os import path
import Microfone as m
import comandos

mic = m.cMicrofone()

alfabeto = list(string.ascii_lowercase)
caminho = path.join(path.expanduser("~"))

diretorio = ""
diretorio_anterior = ""


while (True):
    comandos.falar("Qual disco inicial ?")
    palavra = mic.Ouvir()
    print(palavra)

    # palavra = input('Qual disco inicial: ')

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
                    diretorio = diretorio_anterior
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