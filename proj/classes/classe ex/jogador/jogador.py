class Jogador:

    nome:str
    pontuacao:int = 0

    def __init__(self, nome:str, potuacao:int = 0):
        self.nome = nome
        self.pontuacao = 0

    def acertou_alvo(self, distancia_do_centro):
        if distancia_do_centro < 5:
            self.pontuacao = self.pontuacao + 100

        if distancia_do_centro >= 5 and distancia_do_centro <= 20:
            self.pontuacao = self.pontuacao + 50

        else:
            return self.pontuacao + 10