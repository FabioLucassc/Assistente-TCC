import speech_recognition as sr

# Reconhecedor de voz
reconhecedor = sr.Recognizer()

# Utilizar o microfone para capturar audio
with sr.Microphone() as source:

    while True:
        audio = reconhecedor.listen(source)
        print(reconhecedor.recognize_google(audio, language='pt'))