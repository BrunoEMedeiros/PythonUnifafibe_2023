from produto import *
from utils import *
import os

teste = False

while(not(teste)):
    opcao = menu()
    if opcao == 1:
        for produto in produtos:
            print(f' {produto}')
        teste = sair(input("\n Deseja sair? y/n: "))
        os.system('cls')  
            



