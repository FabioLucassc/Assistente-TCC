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
diretorio1 ="C:"
# print(os.listdir(diretorio1))
while(True):
   palavra = input('Diretorio: ')
   if(palavra == "D:"):
       palavra = ""
       diretorio1 = "D:\\"
       print(os.listdir(diretorio1))
   else:
       diretorio1 += "\\"+palavra
       print(os.listdir(diretorio1))
