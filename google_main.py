import os

import pyttsx3
import speech_recognition as sr
from numpy.core._dtype import __str__
from unidecode import unidecode

from pln.calssificador import classificar
import comandos

# Reconhecedor de voz
reconhecedor = sr.Recognizer()

### ----------- TEXTO EM VOZ ----------- ###

engine = pyttsx3.init()  # object creation

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def falar(texto):
    engine.say(texto)
    engine.runAndWait()


### ----------- TEXTO EM VOZ ----------- ###

# Utilizar o microfone para capturar audio
with sr.Microphone() as source:
    while True:
        try:

            audio = reconhecedor.listen(source)
            resultado = (reconhecedor.recognize_google(audio, language='pt-BR')).lower()

            if resultado is not None:

                resultado = unidecode(resultado)
                # falar(reconhecedor.recognize_google(audio, language='pt-BR'))

                # Reconhecer a qual grupo pertence o comando
                grupo = classificar(resultado)

                if grupo == 'retornarHorario|retornarHorario':
                    falar(comandos.SystemInfo.obter_horario())

                elif grupo == 'retornarData|retornarData':
                    falar(comandos.SystemInfo.obter_data())
                    
                    # Abrir softwares listados
                elif grupo == 'abrir|notepad':
                    falar('Abrindo o bloco de notas')
                    os.system('notepad.exe')

                elif grupo == 'abrir|abrirNavegador':
                    falar('Abrindo o navegador')
                    comandos.SystemInfo.abrir_navegador()

                    # Abrir softwares sites
                elif grupo == 'abrir|acessarGoogle':
                    falar('Acessando Google')
                    comandos.SystemInfo.abrir_google()

                elif grupo == 'abrir|acessarYoutube':
                    falar('Acessando Youtube')
                    comandos.SystemInfo.abrir_youtube()

                elif grupo == 'abrir|acessarFacebook':
                    falar('Acessando Facebook')
                    comandos.SystemInfo.abrir_facebook()

                elif grupo == 'abrir|acessarInstagram':
                    falar('Acessando Instragram')
                    comandos.SystemInfo.abrir_instagram()




                # falar(resultado e a qual grupo ele pertence)
                print('Texto: {} - Grupo: {}'.format(resultado, grupo))



        except Exception:
            print(Exception)
