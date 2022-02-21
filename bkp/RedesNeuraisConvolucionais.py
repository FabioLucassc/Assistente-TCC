import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import zipfile
import numpy as np
import time

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

#zip_object = zipfile.ZipFile(file='personagens.zip', mode='r')
#zip_object.extractall('./')
#zip_object.close()

#'D:\Imagens\TCC\Imagens Time Futebol\Treinamento'
#'D:\Imagens\TCC\Imagens Time Futebol\Teste'

def Treinar(caminhoTreinamento, caminhoTreino, x, y, filtros, epocas):

    inicio = time.time()

    gerador_treinamento = ImageDataGenerator(rescale=1./255, rotation_range=7, horizontal_flip= True, zoom_range=0.2 )

    base_treinamento = gerador_treinamento.flow_from_directory(caminhoTreinamento, target_size=(x,y), batch_size=8, class_mode='categorical')
    base_teste = gerador_treinamento.flow_from_directory(caminhoTreino, target_size=(x,y), batch_size=8, class_mode='categorical', shuffle=False )

    #base_treinamento = gerador_treinamento.flow_from_directory('training_set', target_size=(64,64), batch_size=8, class_mode='categorical')
    #base_teste = gerador_treinamento.flow_from_directory('test_set', target_size=(64,64), batch_size=8, class_mode='categorical', shuffle=False )

    rede_neural = Sequential()
    rede_neural.add(Conv2D(filtros, (3,3), input_shape=(x,y,3), activation='relu'))
    rede_neural.add(MaxPool2D(pool_size=(2,2)))

    rede_neural.add(Conv2D(filtros, (3,3), activation='relu'))
    rede_neural.add(MaxPool2D(pool_size=(2,2)))

    rede_neural.add(Conv2D(filtros, (3,3), activation='relu'))
    rede_neural.add(MaxPool2D(pool_size=(2,2)))

    rede_neural.add(Conv2D(filtros, (3,3), activation='relu'))
    rede_neural.add(MaxPool2D(pool_size=(2,2)))

    rede_neural.add(Flatten())

    rede_neural.add(Dense(units=8, activation='relu'))
    rede_neural.add(Dense(units=8, activation='relu'))

    #rede_neural.add(Dense(units=1, activation='sigmoid'))
    rede_neural.add(Dense(units=base_treinamento.num_classes.numerator, activation='softmax'))

    rede_neural.compile(optimizer='adam', loss='categorical_crossentropy', metrics= ['accuracy'])

    rede_neural.fit(base_treinamento, epochs=epocas, shuffle=True, steps_per_epoch=-1)

    fim = time.time()

    previsoes = rede_neural.predict(base_teste)
    previsoes2 = np.argmax(previsoes, axis=1)

    i = 0
    print('')

    for result in previsoes2:
        print(f"Imagem [{base_teste.filenames[i]}] - {get_key(base_treinamento.class_indices, result)}")
        i += 1

    print('')
    print(f'Total de imagens de teste: {previsoes2.size} | Resolução imagens de treinamento: {x} x {y} | Filtros: {filtros} | Épocas: {epocas} | Tempo de Treinamento: {fim - inicio}')

    #print(accuracy_score(previsoes2, base_treinamento.classes))