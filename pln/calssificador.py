from tensorflow.keras.models import load_model
import numpy as np

# modelo = load_model('pln\modelo.py')
modelo = load_model('model.h5')


labels = open('labels.txt', 'r', encoding='utf-8').read().split('\n')

transformar_label2index = {}
transformar_index2label = {}

for k, label in enumerate(labels):
    transformar_label2index[label] = k
    transformar_index2label[k] = label

# Classificar texto em um entidade
def classificar(text):
    # Criar um array de entrada
    x = np.zeros((1, 48, 256), dtype='float32')

    # Preencher o array com dados do texto.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    # Fazer a previsão
    out = modelo.predict(x)
    idx = out.argmax()
    return transformar_index2label[idx]