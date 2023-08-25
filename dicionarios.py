
#Como criar um dicionario
dicionarios = {
    "nome" : "bruno",
    "idade" : 19,
    "cidade" : "bebedouro"
}
print(f'Acessando a chave "nome": {dicionarios["nome"]}')

#mudando um valor diretamente
dicionarios["idade"] = 24

#Criando novas chaves
dicionarios.update({"formação" : "sistemas de informação"})

#apagando chaves
del dicionarios["cidade"]
print(f'meu novo dicionario: {dicionarios}')

#Testes para localizar chaves no dicionario
if "cargo" in dicionarios:
    print('Existe cargo nesse dicionario')
else:
    print('Não existe cargo nesse dicionario')

#Acessando diretamente chaves e valores
chaves = dicionarios.keys()
valores = dicionarios.values()
print(chaves, valores)

#Acessar valor com valor padrão se chave não existir
idade = dicionarios.get("cargo", 0) 
print(f'Caso o valor não exista, devolva um valor padrão: {idade}')

#Acessando chave por chave com laço
for chave in dicionarios:
    #chave , valor
    print(chave, dicionarios[chave])

#Acessando valo chave a chave com metodo items()
for chave, valor in dicionarios.items():
    print(chave, valor)

print(f'Retorna o interior do dicionario: {dicionarios.items()}')



