from empresa import Empresa

if __name__ ==  '__main__':

    empresa = Empresa('fonseca')

    empresa.contratar("Ana")
    empresa.contratar("Bruno")
    print(empresa.funcionarios)