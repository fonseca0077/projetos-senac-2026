from proj.heranca_polimorfismo.ex5.imagem import Imagem
from proj.heranca_polimorfismo.ex5.pdf import PDF

if __name__ == '__main__':

    
    img = Imagem()
    pdf = PDF()

    for i in range(1):
        print(img.exibir())
        print(pdf.exibir())
