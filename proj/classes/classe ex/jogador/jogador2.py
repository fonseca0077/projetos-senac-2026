from jogador import Jogador

if __name__ == '__main__':

    jogador = Jogador('fonseca')
    jogador.acertou_alvo(15)
    jogador.acertou_alvo(20)
    print(jogador.pontuacao)
    