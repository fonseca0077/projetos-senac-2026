class Segurança:

    def obter_elemento(self, lista:str, indice:int):
        try:
            return lista[indice]
        except IndexError:
            return('Posição inexistente')