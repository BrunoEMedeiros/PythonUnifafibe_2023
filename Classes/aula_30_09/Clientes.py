
class Clientes:
    def __init__(self, id, nome, telefone):
        self.id = id
        self. nome = nome
        self.telefone = telefone
    
    def mudarTelefone(self, novo_numero):
        if len(novo_numero) != 11:
            print("Telefone invalido")
        else:
            self.telefone = novo_numero

listaCliente = [
    Clientes(1,'bruno',17111111111),
    Clientes(2,'ana',17222222222),
    Clientes(3,'maria',17333333333),
]
