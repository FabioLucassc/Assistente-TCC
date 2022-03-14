import os
import re
import string
import subprocess
from os import path
from unidecode import unidecode
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

    if ((palavra.lower() in alfabeto) or ("de" in palavra.lower())):
        # palavra = ""
        diretorio = "D:\\"

        diretorio_anterior = diretorio

        while (True):

            diretorio_anterior = diretorio


            try:

                lista = os.listdir(diretorio)
                print("Qual diretorio ?\n" + str(lista) + "\n")
                palavra = unidecode((mic.Ouvir()).lower())

                str_match = [x for x in comandos.SystemInfo.lower_lista(lista) if re.search(palavra, x)]

                palavra = str(str_match)
                simbolos = '[]\''

                for i in simbolos:
                    palavra = palavra.replace(i, '')

                diretorio += "\\" + palavra

                # if (('.txt' or '.lnk' or '.exe' or '.docx' or '.xls') in diretorio):
                if ("." in diretorio):
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