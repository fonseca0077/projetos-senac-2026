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
