def gravar_diario(mensagem:str):
    with open('diario.txt', 'w') as arquivo:
        arquivo.write(mensagem)