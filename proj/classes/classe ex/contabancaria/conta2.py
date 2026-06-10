from conta import ContaBancaria

if __name__ == '__main__':

    contabancaria = ContaBancaria('fonseca')
    contabancaria2 = ContaBancaria('felipe')
    contabancaria.depositar(30.0)
    contabancaria.transferir(contabancaria2, 20.0)

    print(contabancaria2.saldo)
    print(contabancaria.saldo)

    
