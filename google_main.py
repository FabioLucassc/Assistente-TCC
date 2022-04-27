import subprocess
from os import path
import pyttsx3
import speech_recognition as sr
from unidecode import unidecode
import Microfone as m
import comandos

mic = m.cMicrofone()

reconhecedor = sr.Recognizer()

# Utilizar o microfone para capturar audio
with sr.Microphone() as source:

    while True:

        palavra = mic.Ouvir()

        if palavra == 'boa noite':

            print("Ouvindo...")
            comandos.boas_vindas()

            try:

                resultado = mic.Ouvir()

                print("Fala Reconhecida: " + str(resultado))

                if resultado != "":
                    comandos.Executar.excutar_comandos(resultado)

            except Exception as e:
                print((type(e).__name__ + ': ' + str(e)))