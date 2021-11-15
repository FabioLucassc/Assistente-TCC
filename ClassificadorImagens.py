import RedesNeuraisConvolucionais as RNC
from tkinter.filedialog import askdirectory


def Classificar():
    caminhoTreinamento = askdirectory()
    caminhoTeste = askdirectory()

    if caminhoTreinamento != '' and caminhoTeste != '':
        print('')
        x = int(input('Resolução x de treinamento: '))
        y = int(input('Resulução y de treinamento: '))
        filtros = int(input('Filtros: '))
        epocas = int(input('Épocas: '))

        RNC.Treinar(caminhoTreinamento, caminhoTeste, x, y, filtros, epocas)