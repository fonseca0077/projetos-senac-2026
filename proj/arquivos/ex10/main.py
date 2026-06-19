from seguranca import fazer_backup_dados

if __name__ == '__main__':

    backup = fazer_backup_dados("dados.csv")

if backup:
    print(f"Backup criado com sucesso: {backup}")