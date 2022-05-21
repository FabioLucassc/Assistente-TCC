import datetime
import os
import re
import string
import subprocess
import webbrowser as wb
from os import path

from unidecode import unidecode

import Microfone as m

import pyttsx3

import comandos
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
        falar('Boa tarde, em que posso ajudar ?')

    elif Horario >= 18 and Horario != 0:
        falar('Boa noite, em que posso ajudar ?')


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

        resposta = 'O valor do Dólar é R$ {}, valor atualizado às {} horas e {} minutos'.format(valor, now.hour,
                                                                                                now.minute)
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
    def buscar_endereco(cep):

        temp_string = cep
        out = temp_string.translate(str.maketrans('', '', string.punctuation))
        numbers = [int(temp) for temp in out.split() if temp.isdigit()]
        cep_limpo = ''.join(char for char in str(numbers) if char.isalnum())

        with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep_limpo}/json/") as url:
            data = json.loads(url.read().decode())

        resposta = 'O CEP informado está localizado no estado {}, na cidade de {}, no bairro {}, {}'.format(data['uf'],
                                                                                                            data[
                                                                                                                'localidade'],
                                                                                                            data[
                                                                                                                'bairro'],
                                                                                                            data[
                                                                                                                'logradouro'])

        return resposta

    @staticmethod
    def cumprimentar():

        Horario = int(datetime.datetime.now().hour)

        if Horario >= 0 and Horario < 12:
            resposta = 'Olá, Bom dia, tudo bem com você ? espero que sim. Em que posso ajudar ?'

        elif Horario >= 12 and Horario < 18:
            resposta = 'Olá, Boa tarde, tudo bem com você ? espero que sim. Em que posso ajudar ?'

        elif Horario >= 18 and Horario != 0:
            resposta = 'Olá, Boa noite, tudo bem com você ? espero que sim. Em que posso ajudar ?'

        return resposta

    @staticmethod
    def pesquisar_internet(pesquisa):


        remover_palavras = ['pesquisar', 'pesquise', 'busque', 'buscar', 'procure', 'procurar']
        lista_frase = pesquisa.split()

        result = [palavra for palavra in lista_frase if palavra.lower() not in remover_palavras]

        retorno = ' '.join(result)

        return wb.open_new_tab('http://google.com/search?q='+ retorno)

    @staticmethod
    def lower_lista(lista):
        a = (map(lambda x: x.lower(), lista))
        b = list(a)
        return b

    @staticmethod
    def navegacao():
        mic = m.cMicrofone()

        alfabeto = list(string.ascii_lowercase)

        diretorio = ""
        diretorio_anterior = ""
        listadir = []

        while (True):
            comandos.falar("Qual disco inicial ?")
            print("❖ - Assistente: Qual disco inicial ?")
            palavra = mic.Ouvir()
            print('🎤 - Audio captado: '+palavra)

            # if ((palavra.lower() in alfabeto) or ("de" in palavra.lower())):

            if "de" in palavra.lower():

                diretorio = "D:\\"

            elif((" c" in palavra.lower()) or ("se" in palavra.lower())):

                diretorio = "C:\\"
            else:
                print('🎤 - Audio captado: '+ palavra)
                print("❖ - Assistente: Desculpe, Não consegui encontrar o disco... \n ❖ - Assistente: Saindo do modo navegação por diretórios")
                print('\n________________________________\n')
                falar("Desculpe, Não consegui encontrar o disco...")
                falar("Saindo do modo navegação por diretórios")
                break


            diretorio_anterior = diretorio

            listadir.append(diretorio_anterior)

            while (True):

                diretorio_anterior = diretorio

                try:

                    lista = os.listdir(diretorio)
                    comandos.falar("Qual diretório?")
                    print('\n________________________________\n')
                    print("\n❖ - Assistente:Qual diretorio ?\n"
                          +'________________________________\n'
                          +str(lista)
                          + '________________________________\n\n')
                    palavra = unidecode((mic.Ouvir()).lower())
                    print('🎤 - Audio captado: '+palavra)

                    if palavra == "voltar" and len(listadir) > 1:
                        diretorio = listadir.__getitem__(len(listadir) - 2)
                        listadir.remove(listadir.__getitem__(len(listadir) - 1))
                    else:
                        str_match = [x for x in comandos.SystemInfo.lower_lista(lista) if re.search(palavra, x)]

                        palavra = str(str_match)
                        simbolos = '[]\''

                        if (str_match.__len__() > 1):
                            dirduplicado = (f"Foram encontrados os seguintes diretórios: {str(str_match)}. Diga qual deles deseja acessar.")
                            print('❖ - Assistente: ' +dirduplicado)
                            comandos.falar(dirduplicado)

                            while True:
                                diroficial = mic.Ouvir()
                                palavra = [x for x in comandos.SystemInfo.lower_lista(lista) if diroficial == x]
                                if (palavra != ''):
                                    break

                        for i in simbolos:
                            palavra = palavra.replace(i, '')

                        if palavra != "":
                            diretorio += "\\" + palavra

                    # if (('.txt' or '.lnk' or '.exe' or '.docx' or '.xls') in diretorio):
                    if ("." in diretorio):
                        os.startfile(diretorio)
                        diretorio = diretorio_anterior
                    else:
                        os.listdir(diretorio)
                        if not listadir.__contains__(diretorio):
                            listadir.append(diretorio)

                    print(listadir)

                except:
                    print("❖ - Assistente: diretorio não encontrado")
                    if (diretorio == palavra.upper() + ":\\"):
                        print("Por favor selecione um disco válido!")
                        break
                    diretorio = diretorio_anterior

            else:
                print('Por favor selecione um disco válido!')

class Executar:

    @staticmethod
    def excutar_comandos(frase):

        grupo = classificar(frase)
        fala = ''

        if grupo == 'horario|retornarHorario':
            fala = SystemInfo.obter_horario()
            falar(fala)
        elif grupo == 'data|retornarData':
            fala = SystemInfo.obter_data()
            falar(fala)
            # Abrir softwares listados
        elif grupo == 'cumprimento|responderCumprimento':
            fala = SystemInfo.cumprimentar()
            falar(fala)
            # Abrir softwares listados
        elif grupo == 'abrir|notepad':
            fala = 'Abrindo o bloco de notas'
            falar(fala)
            subprocess.Popen('notepad.exe')
        elif grupo == 'abrir|abrirNavegador':
            fala = 'Abrindo o navegador'
            falar(fala)
            SystemInfo.abrir_navegador()
            # Abrir softwares sites
        elif grupo == 'abrir|acessarGoogle' and 'google' in frase:
            fala = 'Acessando Google'
            falar(fala)
            SystemInfo.abrir_google()
        elif grupo == 'abrir|acessarGoogle' and 'google' not in frase:
            fala = 'Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!'
            falar(fala)
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'abrir|acessarYoutube' and 'youtube' in frase:
            fala = 'Acessando Youtube'
            falar(fala)
            SystemInfo.abrir_youtube()
        elif grupo == 'abrir|acessarYoutube' and 'youtube' not in frase:
            fala = 'Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!'
            falar(fala)
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'abrir|acessarFacebook' and 'facebook' in frase:
            fala = 'Acessando Facebook'
            falar(fala)
            SystemInfo.abrir_facebook()
        elif grupo == 'abrir|acessaracebook' and 'facebook' not in frase:
            fala = 'Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!'
            falar(fala)
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'abrir|acessarInstagram' and 'instagram' in frase:
            fala = 'Acessando Instragram'
            falar(fala)
            SystemInfo.abrir_instagram()
        elif grupo == 'abrir|acessarInstagram' and 'instagram' not in frase:
            fala = 'Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!'
            falar(fala)
            SystemInfo.pesquisar_internet(frase)
        elif (grupo == 'cotacao|retornarCotacaoAtual') and 'dolar' in frase:
            falar('Buscando valor atual do dólar ...')
            fala = SystemInfo.obter_dolar()
            falar(fala)
        elif (grupo == 'cotacao|retornarCotacaoAtual') and 'euro' in frase:
            falar('Buscando valor atual do euro ...')
            fala = SystemInfo.obter_dolar()
            falar(fala)
        elif grupo == 'pesquisa|buscarCep':
            falar('Buscando o CEP informado ...')
            fala = SystemInfo.buscar_endereco(frase)
            falar(fala)
        elif grupo == 'pesquisa|pesquisaWeb':
            fala = 'Ok, já estou pesquisando o\'que você me disse!'
            falar(fala)
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'navegacao|navegarDiretorio':
            falar('Ok, abrindo a navegação por diretório!')
            SystemInfo.navegacao()

        # Mostrar informações (resultado e a qual grupo ele pertence)
        print("\n\n❖ - Assistente: Ouvindo...")
        print('\n________________________________\n')
        print('🎤 - Audio captado: {} - Grupo: {}\n'.format(frase, grupo))
        print('\n________________________________\n')
        print('❖ - Assistente: '+fala)
