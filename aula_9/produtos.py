
class Produtos:
    def __init__(self, id, descricao, preco):
        self.id = id
        self.descricao = descricao
        self.preco = preco

    def __str__(self) -> str:
        return (f'{self.id} {self.descricao} {self.preco}')        