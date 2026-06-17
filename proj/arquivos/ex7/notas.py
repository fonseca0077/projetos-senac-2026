def calcular_medias_alunos():
   
    try:
        nomes_e_medias = [{}]
        caminho_arquivo = 'proj/arquivos/arquivos_teste/notas.txt'
        with open(caminho_arquivo) as arquivo:
            for linhas in arquivo.readlines():
                dados = linhas.split(',')
                nome = dados[0]
                nota1 = float(dados[1]) 
                nota2 = float(dados[2])
                media = (nota1 + nota2) /2

                nomes_e_medias.append({'nome':nome, 'media':media})
    except FileNotFoundError:
        print('Arquivo não encontrado!!!')
        return
    finally:
        if not nomes_e_medias:
            return None
        
        with open('mostrar_medias_finais.txt', 'w') as arquivo:
            for objeto in nomes_e_medias:
                arquivo.write(f"{objeto.get('nome')}, {objeto.get('media')}")


if __name__ == '__main__':

    calcular_medias_alunos()

       

       