from proj.heranca_polimorfismo.ex10.heroi import Heroi
from proj.heranca_polimorfismo.ex10.mago import Mago
from proj.heranca_polimorfismo.ex10.gurreiro import Guerreiro

if __name__ == '__main__':

    heroi = Heroi("João", 100)
mago = Mago("Merlin", 80, 30)
guerreiro = Guerreiro("Conan", 120, 25)

print(heroi.atacar())      
print(mago.atacar())       
print(guerreiro.atacar())

# Heroi possui os atributos nome e vida.
# Mago herda de Heroi e adiciona poder_magico.
# Guerreiro herda de Heroi e adiciona forca_fisica.
# O método atacar() é sobrescrito nas subclasses para calcular o dano conforme solicitado. #