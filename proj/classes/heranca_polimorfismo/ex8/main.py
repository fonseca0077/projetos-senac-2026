from impostorartigodeluxo import ImpostoArtigoLuxo
from calculadordeimposto import CalculadorDeImposto

if __name__ == '__main__':

    calculadordeimposto = CalculadorDeImposto()
    impostoartigoluxo = ImpostoArtigoLuxo()

    valor = 1000
    print(calculadordeimposto.calcular(valor))
    print(impostoartigoluxo.calcular(valor))