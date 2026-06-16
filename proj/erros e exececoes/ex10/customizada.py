class IdadeInvalidaError(Exception):
    pass

    def cadastrar_eleitor(idade:int):
        if idade < 16:
            raise IdadeInvalidaError('Idade inválida')
        print('Cadastro realizado')
