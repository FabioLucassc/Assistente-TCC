import os
import subprocess
from os import path

from speech_recognition import Microphone

caminho = path.join(path.expanduser("~"))
# print(caminho)
diretorio = "C:"
# for teste in os.listdir(diretorio):
#     print(teste)
# print(os.listdir(diretorio))

# print(diretorio)
palavra = ""
diretorio1 =""
# print(os.listdir(diretorio1))
while(True):
   diretorio1 += palavra
   palavra = input('Diretorio: ')
   if(palavra == "D:"):
       palavra = ""
       diretorio1 = "D:\\"
       print(os.listdir(diretorio1))
   else:
     break