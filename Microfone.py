import speech_recognition as sr
from unidecode import unidecode

reconhecedor = sr.Recognizer()



class cMicrofone:

    def Ouvir(self):

        with sr.Microphone() as source:
            reconhecedor.adjust_for_ambient_noise(source, 3)
            # print("Listening....")
            while (True):

                try:

                    # audio = reconhecedor.listen(source, phrase_time_limit=6, timeout=6)
                    audio = reconhecedor.listen(source)
                    resultado = reconhecedor.recognize_google(audio, language='pt-BR')

                    # resultado = (reconhecedor.recognize_google(audio, language='pt-BR', show_all=True))

                    if resultado is not None:

                        resultado = unidecode(resultado).lower()

                        return resultado

                except Exception as e:
                    print(f'Não foi possível identificar a fala. Fale novamente.')
