from imagem import Imagem
from pdf import PDF

if __name__ == '__main__':

    
    img = Imagem()
    pdf = PDF()

    for i in range(1):
        print(img.exibir())
        print(pdf.exibir())
