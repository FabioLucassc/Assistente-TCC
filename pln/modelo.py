import yaml
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.utils import to_categorical


dados = yaml.safe_load(open('treinamento.yml', 'r', encoding='utf-8').read())
entradas, saidas = [], []

for comando in dados['comandos']:
    entradas.append(comando['entrada'].lower())
    saidas.append('{}\{}'.format(comando['grupo'], comando['acao']))

# Processamento de texto: palavras, caracteres, bytes, sub --------------------------------------------------------------
chars = set()

for input in entradas + saidas:
    for ch in input:
        if ch not in chars:
            chars.add(ch)
print('',len(chars))
# Processamento de texto: palavras, caracteres, bytes, sub-palavras -------------------------------------------------------------



# Mapear char-idx -------------------------------------------------------------
caractere_index = {}
index_caractere = {}

for i, ch in enumerate(chars):
    caractere_index[ch] = i
    index_caractere[i] = ch

maior_sequencia = max([len(x) for x in entradas])

print('Número de chars:', len(chars))
print('Maior seq:', maior_sequencia)
# Mapear char-idx -------------------------------------------------------------


# Criar dataset one-hot (número de examplos, tamanho da seq, num caracteres)
# Criar dataset disperso (número de examplos, tamanho da seq)

# Input Data one-hot encoding -----------------------------------------------------------------------

dados_entrada = np.zeros((len(entradas), maior_sequencia, len(chars)), dtype='int32')

for i, input in enumerate(entradas):
    for k, ch in enumerate(input):
        dados_entrada[i, k, caractere_index[ch]] = 1.0

# Input Data one-hot encoding -----------------------------------------------------------------------

# Output Data ------------------------------------------------------------------------
labels = set(saidas)

label_index = {}
index_label = {}

for k, label in enumerate(labels):
    label_index[label] = k
    index_label[k] = label

dados_saida = []

for saida in saidas:
    dados_saida.append(label_index[saida])

output_data = to_categorical(dados_saida, len(dados_saida))

print(output_data[0])
