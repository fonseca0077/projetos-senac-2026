class Personagem:

    nome:str
    vida:int
    ataque:int

    def __init__(self, nome:str, vida:int, ataque:int):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
        self.vida > 0
        return True
    
    def receber_dano(self, quantidade:int):
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0

    def atacar(self, oponente:str):
        if self.esta_vivo:
            oponente.receber_dano(self.ataque)