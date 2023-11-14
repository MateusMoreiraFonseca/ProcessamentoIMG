import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import os

# Abre uma caixa de diálogo para selecionar um arquivo de imagem
filename = filedialog.askopenfilename(initialdir=os.getcwd())

if filename:
    # Verifica se um arquivo válido foi selecionado
    img = cv2.imread(filename)    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    
    if img is not None:
        # A imagem foi carregada com sucesso
        plt.imshow(img)
        plt.title('Exemplo')
        plt.show() 
    else:
        print("Erro: Não foi possível carregar a imagem.")
else:
    print("Nenhum arquivo de imagem selecionado.")
 