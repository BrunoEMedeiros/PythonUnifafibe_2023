# Lendo arquivos txt em python
arquivo = open("teste.txt", "r")

conteudo = arquivo.read()
print(conteudo)

arquivo.close()

# Lendo linha a linha um arquivo em python
arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

print(linhas)

# Lendo um arquivo de texto e guarando o valor em dicionarios
arquivo = open("nome_arquivo.txt", "r")

dados = {}
for linha in arquivo.readlines():
    chave, valor = linha.split("=")
    dados[chave] = valor

arquivo.close()

print(dados)

