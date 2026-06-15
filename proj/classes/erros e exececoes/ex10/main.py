from customizada import IdadeInvalidaError,cadastrar_eleitor

if __name__ == '__main__':

    try:
        cadastrar_eleitor(10)
    except IdadeInvalidaError as e:
        print('Erro capturado: {e}')