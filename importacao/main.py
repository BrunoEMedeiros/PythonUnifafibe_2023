
import funcoes
from funcoes import Mult

opcao = int(input('Opcao 1|2|3|4: '))
numero_um = float(input(''))
numero_dois = float(input(''))

if opcao == 1:
    print(funcoes.Somar(numero_um, numero_dois))