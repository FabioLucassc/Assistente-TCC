import datetime
import webbrowser as wb

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def obter_horario():
        now = datetime.datetime.now()
        resposta = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return resposta

    @staticmethod
    def obter_data():
        now = datetime.datetime.now()
        resposta = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime("%B"), now.year)
        return resposta

    @staticmethod
    def abrir_chrome():
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        return wb.get(chrome_path)

    @staticmethod
    def abrir_navegador():
        return wb.open_new_tab('')

    @staticmethod
    def abrir_google():
        return wb.open_new_tab('http://www.google.com')

    @staticmethod
    def abrir_youtube():
        return wb.open_new_tab('https://www.youtube.com')

    @staticmethod
    def abrir_facebook():
        return wb.open_new_tab('https://www.facebook.com')

    @staticmethod
    def abrir_instagram():
        return wb.open_new_tab('https://www.instagram.com')

