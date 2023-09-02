
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
# sair = False
# clientes = []

# def Crud(opcao, nome = '', idade = 0, codigo = 0):
#     global clientes, sair
#     if opcao == 1:
#         contador = (len(clientes) + 1)
#         cliente = {
#             'id' : str(contador),
#             'nome' : nome,
#             'idade' : idade
#         }
#         clientes.append(cliente)
#         if input('Sair? y/n: ') == 'y':
#             sair = True
#     if opcao == 2:
#         print(clientes)
#         if input('Sair? y/n: ') == 'y':
#             sair = True
#     if opcao == 3:
#         for registros in clientes:
#             if str(codigo) in registros["id"]:
#                 registros["nome"] = nome
#                 registros["idade"] = idade
#                 break
#         if input('Sair? y/n: ') == 'y':
#             sair = True
#     if opcao == 4:
#         for posicao, registros in enumerate(clientes):
#             if str(codigo) in registros["id"]:
#                 clientes.pop(posicao)
#                 break
#         if input('Sair? y/n: ') == 'y':
#             sair = True
        
# while not(sair):
#     opcao = int(input('Opcao: '))
#     if opcao == 1:
#         nome = input('Nome: ')
#         idade = int(input('Idade: '))
#         Crud(opcao, nome, idade)
#     elif opcao == 2:
#         Crud(opcao)
#     elif opcao == 3:
#         nome = input('Nome: ')
#         idade = int(input('Idade: '))
#         codigo = int(input('Codigo: '))
#         Crud(opcao, nome, idade, codigo)
#     elif opcao == 4:
#         codigo = int(input('Codigo: '))
#         Crud(opcao,codigo=codigo)

# def tabuada(contador, n):
#     print(n * contador)
#     if contador < 10:
#         tabuada(contador + 1, n)

# tabuada(0,2)

# def login(senha):
#     if senha != 123:
#         login(int(input('Digite a senha: ')))
#     else:
#         print('Bem vindo')

# login(int(input('Digite a senha: ')))

def montaDicionario(**args):
    for chave, valor in args.items():
        print(f'chave: {chave} valor: {valor}')

montaDicionario(nome='bruno',tel='123456789')









