def analizar_dimensoes_casa(nome_arquivo:str):

    try:
        perimetro = 0
        area = 0

        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo.readlines():
                for linha, caracter in arquivo.readlines():
                    if caracter == '=':
                        perimetro+= linha.count('=')
                        area  += linha.count(' ')

                        print('A quantidade de perimetro é '('='))
                        print('A área é'(' '))

    except ValueError:
        return 'Planta vazia'

        
                      
        
