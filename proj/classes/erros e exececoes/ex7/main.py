from multiplos import Multiplos

if __name__ == '__main__':

    multiplos = Multiplos()

    try:
        print(multiplos.processar_dados(['a', 'b', 'c'], 2))
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)