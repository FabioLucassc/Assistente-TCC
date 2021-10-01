import bs4 as bs
import urllib.request
import spacy
from spacy.matcher import PhraseMatcher
from unidecode import unidecode

class BaseBusca:
    Acoes = [""]

    def Treinar(self):
        self.Acoes.append('dolar')
        self.Acoes.append('cep')

    def Buscar(self, resultado: str):
        for Acao in self.Acoes:
            if resultado.__contains__(Acao):

                if resultado.__contains__('dolar'):
                    return self.BuscarValorDolar()
                elif resultado.__contains__('cep'):
                    return self.BuscarCep()
            else:
                return ''

    def BuscarValorDolar(self):

        dados = urllib.request.urlopen('https://dolarhoje.com')
        dados = dados.read()

        dados_html = bs.BeautifulSoup(dados, 'html.parser')

        dolar = dados_html.find_all(id='nacional')

        conteudo = ''

        conteudo = [p.attrs['value'] for p in dolar]
        conteudo = ''.join(conteudo)

        return str(f'O dólar hoje está{conteudo}')

    def BuscarCep(self):

        cep = input('Informe o CEP: ')

        dados = urllib.request.urlopen(f'https://viacep.com.br/ws/{cep}/xml/')
        dados = dados.read()

        dados_xml = bs.BeautifulSoup(dados, 'lxml')

        tags = dados_xml.findChildren('xmlcep')

        endereco = {}

        for tag in tags:
            for end in tag.findChildren():
                endereco.setdefault(end.name, str(''))
                endereco[end.name] = end.text

        conteudo = ''

        for e in endereco:
          conteudo += str(f'{e}: {endereco[e]}\n')

        return conteudo
