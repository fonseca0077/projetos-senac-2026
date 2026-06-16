def buscar_letra_na_lista(lista_de_strings, indice_lista, indice_palavra):
    try:
        palavra = lista_de_strings[indice_lista]
        letra = palavra[indice_palavra]
        return letra

    except IndexError as erro:
        print(f"Erro: {str(erro)}")