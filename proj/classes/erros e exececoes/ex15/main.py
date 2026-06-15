from cientifica import Experimental,NumeroNegativoError

if __name__ == '__main__':

    experimental = Experimental()

    try:
        print(experimental.calcular_raiz_quadrada(-2))
    except NumeroNegativoError:
        print('o número não pode ser negativo')