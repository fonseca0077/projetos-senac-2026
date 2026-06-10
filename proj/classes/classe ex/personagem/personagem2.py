from personagem import Personagem

if __name__ == '__main__':

    heroi = Personagem("Herói", 100, 20)
    vilao = Personagem("Vilão", 80, 15)

    heroi.atacar(vilao)

    print(vilao.vida)         
    print(vilao.esta_vivo())  

    heroi.atacar(vilao)
    heroi.atacar(vilao)
    heroi.atacar(vilao)

    print(vilao.vida)         
    print(vilao.esta_vivo())  