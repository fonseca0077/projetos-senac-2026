from proj.heranca_polimorfismo.ex6.contaestudante import ContaEstudante

if __name__ == '__main__':

    contaestudante = ContaEstudante(100)
    contaestudante.render_bonus()
    print(contaestudante.saldo)