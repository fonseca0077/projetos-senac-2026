from excecao import entrada_errada, ErroDeEntradaInvalida

if __name__ == '__main__':

    try:
        print(entrada_errada('param'))
    except ErroDeEntradaInvalida:
        print('Valor inválido, o valor deveria ser param')
    

    