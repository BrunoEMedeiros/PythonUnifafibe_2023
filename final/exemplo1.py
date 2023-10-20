import pandas as pd

# Lendo e fechando um arquivo Excel
with pd.ExcelFile("teste1.xlsx") as f:
    # O metodo ExcelFile apenas converte o conteudo do arquivo excel em um
    # objeto DataFrame, portando para realmente acessar e usar seus valores
    # precisar usar o metodo read_excel()

    # Lendo o DataFrame gerado
    # Obs: ele sempre le por default a primeira planilha do arquivo
    data_frame = pd.read_excel(f)

    # Lendo apenas a planilha que eu quero
    data_frame = pd.read_excel(f, sheet_name='Planilha2')

    # Lendo apenas as colunas que eu quero
    # Obs: Quantas colunas eu quiser
    data_frame = pd.read_excel(f, usecols=['alunos'])

    # Lendo da planilha que eu quero dentro do arquivo, e a coluna que eu quero
    data_frame = pd.read_excel(f, sheet_name='Planilha2', usecols=['Horario'])

    print(data_frame)

    # Desativando indice
    print(data_frame.to_string(index=False))
    # Usando with o arquivo é automaticamente fechado quando o escopo termina



