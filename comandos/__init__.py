import datetime
import os
import string
import subprocess
import webbrowser as wb
import pyttsx3
from pln.calssificador import classificar
import urllib.request, json

### ----------- TEXTO EM VOZ ----------- ###
engine = pyttsx3.init()  # object creation

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 135)

def falar(texto):
    engine.say(texto)
    engine.runAndWait()
### ----------- TEXTO EM VOZ ----------- ###

def boas_vindas():

    Horario = int(datetime.datetime.now().hour)

    if Horario >= 0 and Horario < 12:
        falar('Bom dia, em que posso ajudar ?')

    elif Horario >= 12 and Horario < 18:
         falar('Bom tarde, em que posso ajudar ?')

    elif Horario >= 18 and Horario != 0:
        falar('Bom noite, em que posso ajudar ?')

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

    @staticmethod
    def obter_dolar():
        with urllib.request.urlopen("https://economia.awesomeapi.com.br/json/last/USD-BRL") as url:
            data = json.loads(url.read().decode())

        now = datetime.datetime.now()
        valor = round(float(data['USDBRL']['ask']), 2)

        resposta = 'O valor do Dólar é R$ {}, valor atualizado às {} horas e {} minutos'.format(valor, now.hour, now.minute)
        return resposta

    @staticmethod
    def obter_euro():
        with urllib.request.urlopen("https://economia.awesomeapi.com.br/json/last/EUR-BRL") as url:
            data = json.loads(url.read().decode())

        now = datetime.datetime.now()
        valor = round(float(data['EURBRL']['ask']), 2)

        resposta = 'O valor do Euro é R$ {}, valor atualizado às {} horas e {} minutos'.format(valor, now.hour,
                                                                                                now.minute)
        return resposta

    @staticmethod
    def buscar_endereço(cep):

        temp_string = cep
        out = temp_string.translate(str.maketrans('', '', string.punctuation))
        numbers = [int(temp) for temp in out.split() if temp.isdigit()]
        cep_limpo = ''.join(char for char in str(numbers) if char.isalnum())

        with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep_limpo}/json/") as url:
            data = json.loads(url.read().decode())

        resposta = 'O CEP informado está localizado no estado {}, na cidade de {}, no bairro {}, {}'.format(data['uf'],data['localidade'],data['bairro'],data['logradouro'])

        return resposta


class Executar:

    @staticmethod
    def excutar_comandos(frase):

        grupo = classificar(frase)

        if grupo == 'horario|retornarHorario':
            falar(SystemInfo.obter_horario())
        elif grupo == 'data|retornarData':
            falar(SystemInfo.obter_data())

            # Abrir softwares listados
        elif grupo == 'abrir|notepad':
            falar('Abrindo o bloco de notas')
            subprocess.Popen('notepad.exe')
        elif grupo == 'abrir|abrirNavegador':
            falar('Abrindo o navegador')
            SystemInfo.abrir_navegador()

            # Abrir softwares sites
        elif grupo == 'abrir|acessarGoogle' and 'google' in frase:
            falar('Acessando Google')
            SystemInfo.abrir_google()
        elif grupo == 'abrir|acessarYoutube' and 'youtube' in frase:
            falar('Acessando Youtube')
            SystemInfo.abrir_youtube()
        elif grupo == 'abrir|acessarFacebook' and 'facebook' in frase :
            falar('Acessando Facebook')
            SystemInfo.abrir_facebook()
        elif grupo == 'abrir|acessarInstagram' and 'instagram' in frase:
            falar('Acessando Instragram')
            SystemInfo.abrir_instagram()
        elif (grupo == 'cotacao|retornarCotacaoAtual') and 'dolar' in frase:
            falar('Buscando valor atual do dólar ...')
            falar(SystemInfo.obter_dolar())
        elif (grupo == 'cotacao|retornarCotacaoAtual') and 'euro' in frase:
            falar('Buscando valor atual do euro ...')
            falar(SystemInfo.obter_dolar())
        elif grupo == 'pesquisa|buscarCep':
            falar('Buscando o CEP informado ...')
            falar(SystemInfo.buscar_endereço(frase))


        # # falar(resultado e a qual grupo ele pertence)
        print('Texto: {} - Grupo: {}'.format(frase, grupo))