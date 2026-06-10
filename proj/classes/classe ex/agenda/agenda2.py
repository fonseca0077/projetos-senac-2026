from agenda import Agenda

if __name__ == '__main__':

    agenda = Agenda()

    agenda.salvar_contato("Ana", "99999-1111")
    agenda.salvar_contato("Bruno", "98888-2222")

    print(agenda.buscar_telefone("Ana"))
    print(agenda.buscar_telefone("Bruno"))
    print(agenda.buscar_telefone("Carlos"))