class Erros:

    def verificar_sinal(self, numero:int):
        if numero < 0:
            raise ValueError('O número não pode ser negativo')
        return numero
