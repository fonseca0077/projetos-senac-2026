from proj.heranca_polimorfismo.ex7.violao import Violao
from proj.heranca_polimorfismo.ex7.flauta import Flauta
from proj.heranca_polimorfismo.ex7.bateria import Bateria

if __name__ == '__main__':

    violao = Violao()
    flauta = Flauta()
    bateria = Bateria()

    for i in range(2):
        print(violao.tocar())
        print(flauta.tocar())
        print(bateria.tocar())