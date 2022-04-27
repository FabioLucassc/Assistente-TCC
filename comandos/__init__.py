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
            palavra = mic.Ouvir()
            print(palavra)

            # if ((palavra.lower() in alfabeto) or ("de" in palavra.lower())):

            if "de" in palavra.lower():

                diretorio = "D:\\"

            elif((" c" in palavra.lower()) or ("se" in palavra.lower())):

                diretorio = "C:\\"
            else:
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
                    print("\nQual diretorio ?\n" + str(lista) + "\n")
                    # falar("\nQual diretorio ?\n" + str(lista) + "\n")
                    palavra = unidecode((mic.Ouvir()).lower())
                    # print(palavra)

                    if palavra == "voltar" and len(listadir) > 1:
                        diretorio = listadir.__getitem__(len(listadir) - 2)
                        listadir.remove(listadir.__getitem__(len(listadir) - 1))
                    else:
                        str_match = [x for x in comandos.SystemInfo.lower_lista(lista) if re.search(palavra, x)]

                        palavra = str(str_match)
                        simbolos = '[]\''

                        if (str_match.__len__() > 1):
                            dirduplicado = (f"Foram encontrados os seguintes diretórios: {str(str_match)}. Diga qual deles deseja acessar.")
                            print(dirduplicado)
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
                    print("diretorio não encontrado")
                    if (diretorio == palavra.upper() + ":\\"):
                        print("Por favor selecione um disco válido!")
                        break
                    diretorio = diretorio_anterior

            else:
                print("Por favor selecione um disco válido!")

class Executar:

    @staticmethod
    def excutar_comandos(frase):

        grupo = classificar(frase)

        if grupo == 'horario|retornarHorario':
            falar(SystemInfo.obter_horario())
        elif grupo == 'data|retornarData':
            falar(SystemInfo.obter_data())
            # Abrir softwares listados
        elif grupo == 'cumprimento|responderCumprimento':
            falar(SystemInfo.cumprimentar())
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
        elif grupo == 'abrir|acessarGoogle' and 'google' not in frase:
            falar('Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!')
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'abrir|acessarYoutube' and 'youtube' in frase:
            falar('Acessando Youtube')
            SystemInfo.abrir_youtube()
        elif grupo == 'abrir|acessarYoutube' and 'youtube' not in frase:
            falar('Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!')
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'abrir|acessarFacebook' and 'facebook' in frase:
            falar('Acessando Facebook')
            SystemInfo.abrir_facebook()
        elif grupo == 'abrir|acessaracebook' and 'facebook' not in frase:
            falar('Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!')
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'abrir|acessarInstagram' and 'instagram' in frase:
            falar('Acessando Instragram')
            SystemInfo.abrir_instagram()
        elif grupo == 'abrir|acessarInstagram' and 'instagram' not in frase:
            falar('Acho que não entendi muito bem oque você disse, estou realizando uma pesquisa na web para ajudar!')
            SystemInfo.pesquisar_internet(frase)
        elif (grupo == 'cotacao|retornarCotacaoAtual') and 'dolar' in frase:
            falar('Buscando valor atual do dólar ...')
            falar(SystemInfo.obter_dolar())
        elif (grupo == 'cotacao|retornarCotacaoAtual') and 'euro' in frase:
            falar('Buscando valor atual do euro ...')
            falar(SystemInfo.obter_dolar())
        elif grupo == 'pesquisa|buscarCep':
            falar('Buscando o CEP informado ...')
            falar(SystemInfo.buscar_endereco(frase))
        elif grupo == 'pesquisa|pesquisaWeb':
            falar('Ok, já estou pesquisando o\'que você me disse!')
            SystemInfo.pesquisar_internet(frase)
        elif grupo == 'navegacao|navegarDiretorio':
            falar('Ok, abrindo a navegação por diretório!')
            SystemInfo.navegacao()


        # Mostrar informações (resultado e a qual grupo ele pertence)
        print('Texto: {} - Grupo: {}'.format(frase, grupo))
