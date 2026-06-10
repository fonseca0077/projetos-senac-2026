from carrinhodecompras import CarrinhodeCompras

if __name__ == '__main__':

    carrinhodecompras = CarrinhodeCompras()
    carrinhodecompras.adicionar_item('arroz', 350)
    carrinhodecompras.adicionar_item('carne', 350)
    print(carrinhodecompras.calcular_total)