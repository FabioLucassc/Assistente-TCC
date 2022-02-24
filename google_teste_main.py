import os
import subprocess
from os import path
import pyttsx3
import speech_recognition as sr
from unidecode import unidecode

import comandos

reconhecedor = sr.Recognizer()

comandos.boas_vindas()

# Utilizar o microfone para capturar audio
with sr.Microphone() as source:
    while True:

        try:
            audio = reconhecedor.listen(source)
            resultado = (reconhecedor.recognize_google(audio, language='pt-BR')).lower()

            if resultado is not None:

                resultado = unidecode(resultado)

                if resultado != "":
                    comandos.Executar.excutar_comandos(resultado)

        except Exception as e:
            print((type(e).__name__ + ': ' + str(e)))
