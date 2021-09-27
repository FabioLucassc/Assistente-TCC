import pyttsx3
import speech_recognition as sr

# Reconhecedor de voz
reconhecedor = sr.Recognizer()

### ----------- TEXTO EM VOZ ----------- ###

engine = pyttsx3.init() # object creation

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

### ----------- TEXTO EM VOZ ----------- ###

# Utilizar o microfone para capturar audio
with sr.Microphone() as source:

    while True:
        audio = reconhecedor.listen(source)
        print(reconhecedor.recognize_google(audio, language='pt-BR'))
        falar(reconhecedor.recognize_google(audio, language='pt-BR'))