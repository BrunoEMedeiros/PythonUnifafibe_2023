
# #metodo
# def Ola():
#     print('Hello World')

# #funcao
# def meuNome():
#     return 'meu nome é bruno'

# def Somar():
#     return 1 + 2

# res = Somar()

# def Somar(x, y):
#     print(x + y)

# valor = 0
# novo = 'ola'

# def mudarValor():
#     global valor
#     print(f'Dentro da função é {valor}')

# mudarValor()
# print(f'Fora da função é {valor}')

# def Media(n1: float, n2: float) -> float:
#     return 'bruno'

# res = Media(1,2)
# print(res)

# def exibirSaldo(conta = 0, saldo = 0, nome = ''):
#     print(nome)
#     print(conta)
#     if saldo != 0:
#         print(saldo)

# exibirSaldo('bruno','1')
sair = False
clientes = []

def Crud(opcao, nome = '', idade = 0, id = 0):
    global clientes, sair
    if opcao == 1:
        contador = (len(clientes) + 1)
        cliente = {
            'id' : contador,
            'nome' : nome,
            'idade' : idade
        }
        clientes.append(cliente)
        if input('Sair? y/n: ') == 'y':
            sair = True
    if opcao == 2:
        print(clientes)
        if input('Sair? y/n: ') == 'y':
            sair = True

while not(sair):
    opcao = int(input('Opcao: '))
    if opcao != 2:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        Crud(opcao, nome, idade)
    else:
        Crud(opcao)






