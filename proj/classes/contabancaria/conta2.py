from contabancaria import ContaBancaria

if __name__ == '__main__':
    conta = ContaBancaria("fonseca")

    conta.depositar(10)

    assert conta.saldo == 10

    assert conta.sacar(7) is True

    
