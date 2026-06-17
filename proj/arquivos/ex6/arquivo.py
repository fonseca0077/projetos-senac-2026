def somar_valores_arquivo():
    soma = 0.0

    try:
        with open("valores.txt", "r") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                try:
                    valor = float(linha.strip())
                    soma += valor
                except ValueError:
                    print(f"Erro: valor inválido na linha {numero_linha}: '{linha.strip()}'")

        print(f"Soma total: {soma}")

    except FileNotFoundError:
        print("Erro: o arquivo 'valores.txt' não foi encontrado.")