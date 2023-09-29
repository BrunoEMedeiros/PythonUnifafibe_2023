def sair(opcao):
    if opcao == "y":
        return True
    if opcao == "n":
        return False

def menu():
    print('\n Bem vindo!:')
    print('\n 1. Todos os produtos \n 2. Novo Produto \n 3. Sair \n')
    return int(input(" Opcao: "))
