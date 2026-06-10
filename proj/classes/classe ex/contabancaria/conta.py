class ContaBancaria:

    titular:str
    saldo:float

    def __init__(self, titular:str):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor:float):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo - valor > 0:
            return True
        return False
    
    def transferir(self, conta_destino: "ContaBancaria", valor: float):
        if self.saldo < valor:
            return False
        
        self.saldo -= valor
        conta_destino.depositar(valor)
        return True

    




   

        
  
        
