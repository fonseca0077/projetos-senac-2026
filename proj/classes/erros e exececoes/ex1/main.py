from divisao import Divisao
import traceback

if __name__ == '__main__':

    divisao = Divisao()

    try:
        divisao.dividir_numero(1,0)
    except ZeroDivisionError as error:
        print(traceback.format_exc())
    finally:
        b = int(input('Digite um novo número maior que zero:'))
        print(divisao.dividir_numero(1,b))
