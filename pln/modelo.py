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
    saidas.append('{}|{}'.format(comando['grupo'], comando['acao']))

# Processar textos reconhecido : palavras, caracteres, bytes ...

maior_sequencia = max([len(bytes(x.encode('utf-8'))) for x in entradas])

print('Maior seq:', maior_sequencia)

# Criar dataset one-hot (número de examplos, tamanho da seq, num caracteres)

# entrada de dados one-hot encoding

dados_entrada = np.zeros((len(entradas), maior_sequencia, 256), dtype='float32')
for i, inp in enumerate(entradas):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        dados_entrada[i, k, int(ch)] = 1.0

# falar(resultado)
# saida de dados

labels = set(saidas)

fwrite = open('..\labels.txt', 'w', encoding='utf-8')

transformar_label2index = {}
transformar_index2label = {}

for k, label in enumerate(labels):
    transformar_label2index[label] = k
    transformar_index2label[k] = label
    fwrite.write(label + '\n')
fwrite.close()

saida_dados = []

for saida in saidas:
    saida_dados.append(transformar_label2index[saida])

saida_dados = to_categorical(saida_dados, len(saida_dados))

print(saida_dados[0])

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(saida_dados), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(dados_entrada, saida_dados, epochs=500)

# Salvar model
model.save('..\model.h5')


# Classificar texto em um grupo
def classificar(text):
    # Criar um array de entrada
    x = np.zeros((1, 48, 256), dtype='float32')

    # Preencher o array com dados do da frase.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    # Fazer a predição do que foi falado
    saida = model.predict(x)
    index = saida.argmax()
    print(transformar_index2label[index])


while True:
    frase = input('Escreva Algo: ')
    classificar(frase)
