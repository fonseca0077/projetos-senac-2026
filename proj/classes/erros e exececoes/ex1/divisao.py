class Divisao:

    def dividir_numero(self,a:int, b:int):
        if b == 0:
            raise ZeroDivisionError('Não é possível dividir por zero')
        
        return a/b