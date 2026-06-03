################# Exercícios (1ª aula) #################

def calcula_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def converte_temperatura_fahrenreit(graus_celsius: float):
    temperatura = (graus_celsius * (9/5)) + 32
    print(f"A temperatura em fahrenreit é: {temperatura}")

def converte_em_dolares(reais: float):
    dolares = reais / 5.04
    print(f"O valor em dólares é: {dolares}")

    ################# Exercícios (2ª aula) #################

    def classificar_pop(idade: int) -> str:

        if idade <= 12:
            return "Criança"
        
        if idade > 12 and idade < 18:
            return "Adolescente"
        
        if idade >= 18 and idade <= 60:
            return "Adulto"
        
        else:
            return "idoso"
        
##########################################################

def eh_par(numero: int):
                
    if numero %2 == 0:
        return True
    return False

##########################################################

def classifica_idade(idade: int):
     if idade <= 12:
        return "Criança"
        
     if idade > 12 and idade < 17:
        return "Adolescente"
     
     else:
        return "Adulto"

##########################################################

def calcular_bonus(salario: float, anos_empresa: int):
    if anos_empresa > 5:
        return salario * 0.1
    else:
        return salario * 0.05
    
############################################################

def encontrar_maior(a: int, b: int, c:int):
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    if c > b and c > a:
        return c
    
###########################################################

def tipo_triangulo(lado1:float , lado2:float , lado3:float):
    if lado1 + lado2 > lado3 or lado3 + lado1 > lado2 or lado3 + lado2 > lado1:
        return "Não é triângulo"
    
    if lado1 == lado2 == lado3:
        return "Equilátero"
    
    if lado1 != lado2 != lado3:
        return "Escaleno"
    
    else:
        return  "Isóceles"
    
############################################################

def aprovar_saque(saldo:float, valor_saque: float):

    if valor_saque <= saldo and valor_saque % 10 == 0:
        return True
    return False

 ################# Exercícios (3ª aula) #################

frutas = ['maçã', 'banana', 'laranja', 'morango']

def primeira_fruta(frutas: list):
    return frutas[0]


###########################################################

animais = ['gato', 'cachorro', 'passarinho', 'coelho']

def ultimo_animal(animais: list):
    return animais[-1]


##############################################################

compras = []

def adicionar_compras(compras: list):
    compras.append('arroz')
    compras.append('feijão')
    compras.append('batata')

    return compras

##########################################################

notas = [7.5, 8.0, 6.0, 9.5, 10.0]

def quantidade_notas(notas: list):
    return len(notas)

#############################################################

cores = ['vermelho', 'verde', 'azul']

def mudar_cor(cores: list):
    cores[1] = 'amarelo'
    return cores

############################################################

tarefas = ['estudar', 'limpar quarto', 'lavar louça']

def esvaziar_tarefas(tarefas: list):
    tarefas.clear()
    return tarefas

###########################################################

respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']

def contar_sim(respostas: list):
    return respostas.count('Sim')
    
###########################################################

fila = ['Ana', 'Bruno', 'Carlos', 'Diego']

def remover_ultimo(fila: list):
    fila.pop()
    return (fila)

###########################################################

canais = ['Globo', 'SBT', 'Record', 'Band']

def posicao_sbt(canais: list):
    return canais.index('SBT')
    
#############################################################

dias = ['Segunda', 'Quarta', 'Quinta']

def ajustar_terca(dias: list):
    dias.insert(1,'Terça') 
    return dias

##########################################################

numeros = [10, 20, 30, 40, 50, 60]

def tres_primeiros(numeros: list):
    return numeros[:3]

##########################################################

convidados = ['Alice', 'Bob', 'Arthur', 'Carol']

def remover_arthur(convidados: list):
    convidados.remove('Arthur')
    return convidados

#########################################################

letras = ['A', 'B', 'C', 'D', 'E']

def inverter_lista(letras: list):
    letras.reverse()
    return letras

#########################################################

pontos = [45, 12, 89, 5, 23]

def ordenar_pontos(pontos: list):
    pontos.sort()
    return pontos

#########################################################

valores = [12, 5, 8, 22, 9, 15]

def soma_extremos(valores: list):
    resultado = valores [0] + valores [-1]
    return(resultado)

###########################################################

ingredientes = ['ovo', 'farinha', 'açúcar', 'leite']

def tem_chocolate(ingredientes: list):
    if 'chocolate' in ingredientes:
        return True
    return False

###########################################################

amigos_escola = ['Pedro', 'Lucas'] 
amigos_bairro = ['Mariana', 'Julia']

def juntar_amigos(amigos_escola: list, amigos_bairro:list):
    amigos_escola.extend(amigos_bairro)
    return amigos_escola
    
############################################################

anos = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

def ultimos_tres(anos: list):
    return anos[-3:]

#############################################################

brinquedos = ['carrinho', 'boneca', 'bola', 'pião']

def remover_brinquedo_seguro(brinquedos: list, item: list):
    if item in brinquedos:
        brinquedos.remove(item)
        return brinquedos
    return 'Este brinquedo não está na lista!'


if __name__ == '__main__':
    
    print("Resultado ex 1")
    fruta = primeira_fruta(frutas)
    print(fruta)

    print("\n Resultado ex 2")
    animal = ultimo_animal(animais)
    print(animal)

    print("\n Resultado ex 3")
    compras = adicionar_compras([])
    print(compras)

    print("\n Resultado ex 4")
    notas = quantidade_notas(notas)
    print(notas)

    print("\n Resultado ex 5")
    cores = mudar_cor(cores)
    print(cores)

    print("\n Resultado ex 6")
    tarefas = esvaziar_tarefas(tarefas)
    print(tarefas)

    print("\n Resultado ex 7")
    sim = contar_sim(respostas)
    print(respostas)

    print("\n Resultado ex 8")
    fila = remover_ultimo(fila)
    print(fila)

    print("\n Resultado ex 9")
    canais = posicao_sbt(canais)
    print(canais)

    print("\n Resultado ex 10")
    dias = ajustar_terca(dias)
    print(dias)

    print("\n Resultado ex 11")
    numeros = tres_primeiros(numeros)
    print(numeros)

    print("\n Resultado ex 12")
    convidados = remover_arthur(convidados)
    print(convidados)

    print("\n Resultado ex 13")
    letras = inverter_lista(letras)
    print(letras)

    print("\n Resultado ex 14")
    pontos = ordenar_pontos(pontos)
    print(pontos)

    print("\n Resultado ex 15")
    valores = soma_extremos(valores)
    print(valores)


    print("\n Resultado ex 16")
    ingredientes = tem_chocolate(ingredientes)
    print(ingredientes)


    print("\n Resultado ex 17")
    amigos_escola = juntar_amigos(amigos_escola,amigos_bairro)
    print(amigos_escola)


    print("\n Resultado ex 18")
    anos = ultimos_tres(anos)
    print(anos)


    print("\n Resultado ex 19")
    brinquedos = remover_brinquedo_seguro(brinquedos, item)
    print(brinquedos)


    print("\n Resultado ex 20")



    