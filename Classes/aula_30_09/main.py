from Produtos import *
from Vendas import *
from Clientes import *

print("Bem vindo ao caixa! \n")
Produto.todosProdutos()

print('\n')
carrinho = input("Digite o(s) codigo(s) dos itens: ").split(',')
print('\n')

carrinho_int = []
for item in carrinho:
    carrinho_int.append(int(item))

lista_final = Produto.carrinhoProdutos(carrinho_int)
if input("Confirmar venda: y/n ?") == 'y':
    Vendas(1,"30-09-2023 15:18",lista_final[0],'bruno','maria',lista_final[1],'cartao',1).efetuarVenda()
    Vendas.todasVendas()