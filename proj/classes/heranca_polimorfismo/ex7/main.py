from violao import Violao
from flauta import Flauta
from bateria import Bateria

if __name__ == '__main__':

    violao = Violao()
    flauta = Flauta()
    bateria = Bateria()

    for i in range(2):
        print(violao.tocar())
        print(flauta.tocar())
        print(bateria.tocar())