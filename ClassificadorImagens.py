import RedesNeuraisConvolucionais as RNC
from tkinter.filedialog import askdirectory

caminhoTreinamento = askdirectory()
caminhoTeste = askdirectory()

if caminhoTreinamento != '' and caminhoTeste != '':
    RNC.Treinar(caminhoTreinamento, caminhoTeste)