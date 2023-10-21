import pandas
from produtos import Produtos

lista_produtos = []
with pandas.ExcelFile("arquivo.xlsx") as arquivo:
    data_frame = pandas.read_excel(arquivo)
    
    for indice, coluna in data_frame.iterrows():        
        lista_produtos.append(Produtos(indice, 
                                       coluna["produto"], 

                                       coluna["preco"]))
for produto in lista_produtos:
    print(produto)