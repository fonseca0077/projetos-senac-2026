from livro import Livro

if __name__ == '__main__':
    livro = Livro("killua", "fonseca", 12)
    livro.vender()
    livro.reabastecer(8)
    print(livro.quantidade_copias)
    