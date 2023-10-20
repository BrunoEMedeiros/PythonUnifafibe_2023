import pandas

arquivo =  pandas.read_excel('Pasta1.xlsx')

print(arquivo['Preco'].max())
print(arquivo['Preco'].min())

# Filtrar linhas onde a idade é maior que 30
resultados = arquivo.loc[df['Idade'] > 30]

print(resultados)

# for linhas in arquivo.itertuples():
#     linhas[]