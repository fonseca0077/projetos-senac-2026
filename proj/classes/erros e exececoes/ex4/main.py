from erros import Erros

if __name__ == '__main__':

    erros = Erros()

    #print(erros.verificar_sinal(3))

    try:
        print(erros.verificar_sinal(-3))
    except ValueError:
        print('Número não pode ser menor que zero')
