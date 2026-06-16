from proj.heranca_polimorfismo.ex8.impostorartigodeluxo import ImpostoArtigoLuxo
from proj.heranca_polimorfismo.ex8.calculadordeimposto import CalculadorDeImposto

if __name__ == '__main__':

    calculadordeimposto = CalculadorDeImposto()
    impostoartigoluxo = ImpostoArtigoLuxo()

    valor = 1000
    print(calculadordeimposto.calcular(valor))
    print(impostoartigoluxo.calcular(valor))