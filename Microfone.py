import speech_recognition as sr

reconhecedor = sr.Recognizer()



class cMicrofone:

    def Ouvir(self):

        with sr.Microphone() as source:
            reconhecedor.adjust_for_ambient_noise(source, 1)
            # print("Listening....")
            while (True):
                try:

                    audio = reconhecedor.listen(source)
                    resultado = reconhecedor.recognize_google(audio, language='pt-BR').lower()

                    if resultado is not None:

                        return resultado

                except Exception as e:
                    print((type(e).__name__ + ': ' + str(e.__str__())))
