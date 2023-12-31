import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import os
import sys


def readImage():
    # Abre uma caixa de diálogo para selecionar um arquivo de imagem
    filename = filedialog.askopenfilename(initialdir=os.getcwd())
    if not os.path.isfile(filename):
        sys.exit("Arquivo inválido ou não selecionado.")

    # Verifica se um arquivo válido foi selecionado
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def showImages(img1, img2, img3, tituloSuperior):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle(tituloSuperior)
    ax1.imshow(img1)
    ax2.imshow(img2)
    ax3.imshow(img3)
    ax1.set_title("Imagem 1")
    ax2.set_title("Imagem 2")
    ax3.set_title("Resultado")
    ax1.axis("off")
    ax2.axis("off")
    ax3.axis("off")
    plt.show()


def saveImage(img):
    filename = filedialog.asksaveasfilename(
        initialdir=os.getcwd(), defaultextension=".jpg"
    )

    if not os.path.exists(os.path.dirname(filename)):
        sys.exit("Diretorio Invalido")

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename, img)


def main():
    img1 = readImage()
    img2 = readImage()
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    # print("==IMG1==")
    # print(img1)

    # print("==IMG2==")
    # print(img2)

    img3 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
    saveImage(img3)
    # print("==IMG3==")
    # print(img3)
    showImages(img1, img2, img3, "Adição de imagens")


if __name__ == "__main__":
    main()
