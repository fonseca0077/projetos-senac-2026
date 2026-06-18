def buscar_palavra_no_texto(palavra_alvo):

    with open('documento.txt', 'r') as arquivo:
      
        for indice, linha in enumerate(arquivo.readlines()):
            if linha.find(palavra_alvo):
                print(f"{indice} - {linha}")