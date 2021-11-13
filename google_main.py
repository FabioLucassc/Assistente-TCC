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
            resultado = (reconhecedor.recognize_google(audio, language='pt-BR'))

            if resultado is not None:

                resultado = unidecode(resultado)
                # falar(reconhecedor.recognize_google(audio, language='pt-BR'))

                # Reconhecer a qual grupo pertence o comando

                grupo = classificar(resultado)

                if grupo == 'retornarHorario\\retornarHorario':
                    falar(comandos.SystemInfo.obter_horario())

                # falar(resultado e a qual grupo ele pertence)
                print('Texto: {}-Grupo: {}'.format(resultado, grupo))
        except Exception:
            print(Exception)
