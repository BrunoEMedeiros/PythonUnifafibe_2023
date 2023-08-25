#Listas no python
numeros = [1,2,3,4,5]
texto = ['ola','turma','unifafibe','python']
logico = [True, False, True]

#-------Metodos comuns em listas------------
#Append -> Adicionar itens
numeros.append(6)

#Pop -> Removendo itens da lista
texto.pop()

#removendo por posição
texto.pop(0)

#Remove -> Exclui a primeira ocorrencia do valor indicado na lista
logico.remove(True)

#Copy -> faz uma copia superficial da lista
nova_lista = numeros.copy()

#Clear -> Limpa toda lista
numeros.clear()

#Count -> retorna o total de ocorrencias o item que voce passa
print(f'Numero de ocorrencias de True: {logico.count(True)}')

#Extend -> mesclando listas no python
letras = ['a','b','c','d','e']
texto.extend(letras)

#Index -> retorna o indice do item na primeira ocorrencia em que ele aparece
print(f'A letra b aparece no indice: { texto.index("b") }')

#Insert -> inserindo item por posição em uma lista python
#(posição, valor)
numeros.insert(0,20)
numeros.insert(1,10)
numeros.insert(2,3)
numeros.insert(4,32)

#Sort -> Ordena a lista em ordem crescente
numeros.sort()

#Reverse -> Reverte a lista
nova_lista.reverse()

print(numeros, nova_lista, texto, logico)
