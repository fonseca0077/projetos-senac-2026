from construtor import Construtor

if __name__ == '__main__':

  

    try:

        construtor = Construtor('felipe',-1)

        print(construtor.nome)
        print(construtor.preco)
    except ValueError:
        print('Não pode ser menor que zero')

