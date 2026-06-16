class Construtor:

    nome:str
    preco:float

    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

        if self.preco <= 0:
            raise ValueError