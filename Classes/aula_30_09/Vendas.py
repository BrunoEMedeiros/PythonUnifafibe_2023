 
class Vendas:
    def __init__(self, 
                 id: int, 
                 data_hr: str, 
                 produtos: list, 
                 operador: str, 
                 cliente: str, 
                 valor: float, 
                 forma_pgt: str,
                 pdv: int):
        self.id = int(id)
        self.data_hr = data_hr
        self.produtos = produtos
        self.operador = operador
        self.cliente = cliente
        self.valor = float(f"{valor:.{2}f}")
        self.forma_pgt = forma_pgt
        self.pdv = int(pdv)

    def desconto():
        pass

    def efetuarVenda(self):
        listaVendas.append(self)

    def alterarVenda():
        pass

    def excluirVenda():
        pass

    #Decorator
    @staticmethod
    def todasVendas():
        for vendas in listaVendas:
            print(vendas)

    def listarProdutos(self):
        for produto in self.produtos:
            print(produto)

    def __str__(self) -> str:
        return (f'{self.id},{self.data_hr},{self.listarProdutos()},{self.operador},{self.cliente},{self.valor},{self.forma_pgt},{self.pdv}')

# Vendas.todasVendas()
listaVendas = []

# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()
# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()
# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()
# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()
# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()
# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()
# Vendas(1,'30-09-2023 11:28',[1,2,3],'bruno','jean',50,'cartao',1).efetuarVenda()

# Vendas.todasVendas()