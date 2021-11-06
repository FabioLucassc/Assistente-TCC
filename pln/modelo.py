import yaml
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.utils import to_categorical

dados = yaml.safe_load(open('treinamento.yml', 'r', encoding='utf-8').read())

entradas, saidas = [], []

for comando in dados['comandos']:
    entradas.append(comando['entrada'].lower())
    saidas.append('{}\{}'.format(comando['acao'], comando['acao']))


# Processar texto: palavras, caracteres, bytes, sub-palavras

maior_sequencia = max([len(bytes(x.encode('utf-8'))) for x in entradas])

print('Maior seq:', maior_sequencia)

# Criar dadosset one-hot (número de examplos, tamanho da seq, num caracteres)
# Criar dadosset disperso (número de examplos, tamanho da seq)

# Input dados one-hot encoding

dados_entrada = np.zeros((len(entradas), maior_sequencia, 256), dtype='float32')
for i, inp in enumerate(entradas):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        dados_entrada[i, k, int(ch)] = 1.0


# Input dados sparse
'''
dados_entrada = np.zeros((len(entradas), maior_sequencia), dtype='int32')
for i, input in enumerate(entradas):
    for k, ch in enumerate(input):
        dados_entrada[i, k] = chr2idx[ch]
'''

# Output dados

labels = set(saidas)

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

saida_dados = []

for output in saidas:
    saida_dados.append(label2idx[output])

saida_dados = to_categorical(saida_dados, len(saida_dados))


print(saida_dados[0])

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(saida_dados), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(dados_entrada, saida_dados, epochs=128)

# Classificar texto em um entidade
def classify(text):
    # Criar um array de entrada
    x = np.zeros((1, 48, 256), dtype='float32')

    # Preencher o array com dados do texto.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    # Fazer a previsão
    out = model.predict(x)
    idx = out.argmax()
    print(idx2label[idx])

while True:
    text = input('Digite algo: ')
    classify(text)