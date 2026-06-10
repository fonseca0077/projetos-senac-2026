class Carro:

    modelo:str
    ano:int

    def __init__(self, modelo: str, ano:int):
        self.odometro = 0

    def viajar(self, distancia:float):
        if distancia < 0:
            return "Não pode numero negativo"
        self.odometro = self.odometro + distancia
