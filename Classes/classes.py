
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome  = nome
#         self.idade = idade

#     def meApresentar(self):
#         print(f'Meu nome eh {self.nome} e eu tenho {self.idade} anos')

# class Produto:
#     def __init__(self, cod, nome, preco, marca, modelo):
#         self.cod = cod
#         self.nome = nome
#         self.preco = preco
#         self.marca = marca
#         self.modelo = modelo

# class Monitor(Produto):
#     def __init__(self, cod, nome, preco, marca, modelo, polegada, resolucao):
#         super().__init__(cod, nome, preco, marca, modelo,)
#         self.polegada = polegada
#         self.resulocao = resolucao

# monitor_gamer = Monitor(1,"monitor",500,"samsung","gamer",32,"4k")
# print(monitor_gamer)

# self.marca -> public
# self._marca -> private
# self.__marca -> protected 
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._preco = 0
    
    def verCarro(self):
        print(f'{self.marca} {self.modelo} {self._preco}')

uno = Carro("fiat","uno de firma com escada em cima")
uno.verCarro()
