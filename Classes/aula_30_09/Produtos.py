
class Produto:
    def __init__(self, id, desc, preco, qtd):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.qtd = qtd

    def tirarEstoque(self, qtd):
        if self.qtd - qtd < 0:
            print('Quantidade insuficiente para retirada!')
        else:
            self.qtd -= qtd
    
    def mudarPreco(self, preco):
        if preco <= 0:
            print('O preco nao pode ser igual ou inferior a 0!')
        else:
            self.preco = preco
    
    def mudarDescricao(self, desc: str):
        self.desc = desc if len(desc) <= 10 else print("Numero maximo de caracteres: 10")
    
    @staticmethod
    def todosProdutos():
        for produtos in listaProdutos:
            print(produtos)

    @staticmethod
    def carrinhoProdutos(lista):
        carrinho = []
        total = 0
        for produto in listaProdutos:
            for item in lista:
                if produto.id == item:
                    carrinho.append(produto)
                    total += produto.preco
                    print(produto)
        print(f" Total: {total}")
        return (carrinho, total)
    
    def __str__(self) -> str:
        return (f' {self.id} , {self.desc} , {self.preco} ')

listaProdutos = [
    Produto(1,"amaciante",20,30),
    Produto(2,"coca-cola",5.50,100),
    Produto(3,"banana prata KG",10.25,20),
    Produto(4,"cochao mole KG",40.20,100),
    Produto(5,"jogo de talher",35,40),
]
