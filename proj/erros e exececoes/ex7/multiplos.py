class Multiplos:

    def processar_dados(self, lista:list, indice:int):

        try:
            elemento = lista[indice] /2
        except IndexError:
            return 'Erro de índice'
        except TypeError/ValueError:
            return 'Elemento não é um número'
        
        return elemento
            
