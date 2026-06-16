from polimorfico import AnatomiaError
from polimorfico import Instrumento
from polimorfico import Guitarra

try:
    instrumento = Instrumento()
    print(instrumento.tocar())
except AnatomiaError as erro:
    print(f"Erro: {erro}")

try:
    guitarra = Guitarra()
    print(guitarra.tocar())
except AnatomiaError as erro:
    print(f"Erro: {erro}")