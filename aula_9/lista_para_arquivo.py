import pandas
from produtos import Produtos

lista_produtos = [
    Produtos(1,"coca-cola", 5),
    Produtos(2,"salgadinho", 10),
    Produtos(3,"kg banana prata", 6),
]

lista_dicionarios = []
for produtos in lista_produtos:
    lista_dicionarios.append(produtos.__dict__)

data_frame = pandas.DataFrame(lista_dicionarios).set_index("id")
print(data_frame)
data_frame.to_excel("final.xlsx")