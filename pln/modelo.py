import yaml
import numpy as np


dados = yaml.safe_load(open('treinamento.yml', 'r', encoding='utf-8').read())
entradas, saidas = [], []

for comando in dados['comandos']:
    entradas.append(comando['entrada'].lower())
    saidas.append('{}\{}'.format(comando['grupo'], comando['acao']))

# Processamento de texto: palavras, caracteres, bytes, sub-palavras

chars = set()

for input in entradas + saidas:
    for ch in input:
        if ch not in chars:
            chars.add(ch)
print('',len(chars))



# Mapear char-idx

caractere_index = {}
index_caractere = {}

for i, ch in enumerate(chars):
    caractere_index[ch] = i
    index_caractere[i] = ch


maior_sequencia = max([len(x) for x in entradas])

print('Número de chars:', len(chars))
print('Maior seq:', maior_sequencia)

# Criar dataset one-hot (número de examplos, tamanho da seq, num caracteres)
# Criar dataset disperso (número de examplos, tamanho da seq)

# Input Data one-hot encoding

dados_entrada = np.zeros((len(entradas), maior_sequencia, len(chars)), dtype='int32')
for i, entrada in enumerate(entradas):
    for k, ch in enumerate(entrada):
        dados_entrada[i, k, caractere_index[ch]] = 1.0

print(dados_entrada)