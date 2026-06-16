from carga import ElevadorSobrecargadoError
from carga import Elevador

if __name__ == '__main__':

    elevador = Elevador()

try:
    elevador.entrar_pessoa(120)
    elevador.entrar_pessoa(150)
    elevador.entrar_pessoa(200)  # aqui deve dar erro
except ElevadorSobrecargadoError as erro:
    print(erro)

print("Peso final:", elevador.peso_total)