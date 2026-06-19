def inventariar_moveis(nome_arquivo):

    lista = []

    with open(nome_arquivo) as arquivo:
      for i, linha in enumerate(arquivo):
            linha = linha.rstrip("\n")

            for j, caractere in enumerate(linha):
                if caractere.isalpha() and caractere.isupper():
                    lista.append((caractere, (i, j)))

    # transforma a lista em dicionário
    inventario = {}

    for letra, coordenada in lista:
        if letra not in inventario:
            inventario[letra] = []
        inventario[letra].append(coordenada)

    return inventario