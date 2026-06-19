def fazer_backup_dados(nome_arquivo_original):
    nome_arquivo_backup = f"{nome_arquivo_original}.bak"

    try:
        with open(nome_arquivo_original, "rb") as arquivo_original:
            conteudo = arquivo_original.read()

        with open(nome_arquivo_backup, "wb") as arquivo_backup:
            arquivo_backup.write(conteudo)

        return nome_arquivo_backup

    except PermissionError:
        print(
            f"Erro: sem permissão para criar ou gravar o arquivo de backup "
            f"'{nome_arquivo_backup}'."
        )
    except OSError as erro:
        print(f"Erro de sistema ao realizar o backup: {erro}")

    return None