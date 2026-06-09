from carro import Carro

if __name__  == '__main__':

    carro = Carro('monza', 2011)
    carro.viajar(25.5)
    print(carro.odometro)