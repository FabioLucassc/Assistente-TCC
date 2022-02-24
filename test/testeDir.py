import os
import subprocess
from os import path

from speech_recognition import Microphone

caminho = path.join(path.expanduser("~"))
print(caminho)
diretorio = "C:"
for teste in os.listdir(diretorio):
    print(teste)
print(os.listdir(diretorio))

print(diretorio)