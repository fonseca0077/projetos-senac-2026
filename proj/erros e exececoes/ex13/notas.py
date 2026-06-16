def adicionar_nota_aluno(lista_notas, nova_nota):
    try:
        # Verifica se a nota está dentro do intervalo permitido
        if nova_nota < 0.0 or nova_nota > 10.0:
            raise ValueError("A nota deve estar entre 0.0 e 10.0.")

        lista_notas.append(nova_nota)
        print("Nota adicionada com sucesso!")

    except TypeError:
        print("Erro: tipo de dado incorreto. Informe uma nota numérica.")

    except ValueError as erro:
        print(f"Erro: {erro}")