import pandas as pd
from pessoa import Pessoa

lista = []

with pd.ExcelFile("teste1.xlsx") as f:
    data_frame = pd.read_excel(f);
    # Percorrendo o DataFrame linha a linha para manipula-lo com precisao 
    for indice, coluna in data_frame.iterrows():
        # print(indice, coluna["alunos"], coluna["idades"])

        # Criando objetos da minha classe Pessoa com as linhas do DataFrame
        obj = Pessoa(coluna["alunos"], coluna["idades"])
        lista.append(obj)

for pessoas in lista:
    print(pessoas)