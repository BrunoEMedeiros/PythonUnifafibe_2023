class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return(f'nome: {self.nome}, idade: {self.idade}')
