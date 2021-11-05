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

# Processamento de texto: palavras, caracteres, bytes, sub ---------------------------------------------------------------------
maior_sequencia = max([len(bytes(x.encode('utf-8'))) for x in entradas])
print('Maior seq:', maior_sequencia)

# Processamento de texto: palavras, caracteres, bytes, sub-palavras -------------------------------------------------------------

# Input Data one-hot encoding -----------------------------------------------------------------------

dados_entrada = np.zeros((len(entradas), maior_sequencia, 256), dtype='int32')

for i, entrada in enumerate(entradas):
    for k, ch in enumerate(bytes(entrada.encode('utf-8'))):
        dados_entrada[i, k, int[ch]] = 1.0

# Input Data one-hot encoding -----------------------------------------------------------------------

# Criar dataset one-hot (número de examplos, tamanho da seq, num caracteres)
# Criar dataset disperso (número de examplos, tamanho da seq)

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

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(output_data), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(dados_entrada, dados_saida, epochs=128)

# Classificar texto em um entidade
def classificar(text):
    # Criar um array de entrada
    x = np.zeros((1, 48, 256), dtype='float32')

    # Preencher o array com dados do texto.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    # Fazer a previsão
    out = model.predict(x)
    idx = out.argmax()
    print(index_label[idx])

while True:
    text = input('Digite algo: ')
    classificar(text)