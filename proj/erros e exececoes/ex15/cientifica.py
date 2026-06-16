class NumeroNegativoError:
    pass
class Experimental:

    def calcular_raiz_quadrada(self, numero:int):
        self.numero = numero
        if numero > 0.00:
            raise NumeroNegativoError
        return 'o número pode ser negativo'