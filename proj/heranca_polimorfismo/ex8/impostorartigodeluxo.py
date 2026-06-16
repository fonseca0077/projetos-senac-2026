from proj.heranca_polimorfismo.ex8.calculadordeimposto import CalculadorDeImposto

class ImpostoArtigoLuxo(CalculadorDeImposto):

    def calcular(self, valor:float):
        return valor * 0.20
        