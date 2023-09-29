class Produtos:
    def __init__(self, id: int, desc: str, preco: float, qtd: int):
        self.id = id
        self.desc = desc
        #Obs: python 3.6+
        self.preco = f"{preco:.{2}f}"
        self.qtd = qtd

    def __str__(self):
        return(f'cod: {self.id}, descricao: {self.desc}, preco: {self.preco}, quantidade: {self.qtd}')

produtos = [
    Produtos(1,"tenis",200.50,10),
    Produtos(2,"camisa",110,5),
    Produtos(3,"bone",50.30,12),
]
