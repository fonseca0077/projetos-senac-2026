def contar_linhas_arquivos(self, nome_arquivo:str):
    with open(nome_arquivo) as arquivo:
        contagem = 0
        for linha in arquivo.readlines():
            if linha.find('\n') > 0:
                if linha.endswith('\n') or linha.startswith('\n'):
                    contagem +=1