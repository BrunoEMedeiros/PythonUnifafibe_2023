lista = [1,52,36,5,74,5,8,5,2,82]

print(max(lista))
print(min(lista))
print(sum(lista) / len(lista))

maior = lista[0]
menor = lista[0]
media = 0
for n in lista:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media += n

print(maior)
print(menor)
print(media/len(lista))

nova = sorted(lista)
print(nova[0])
menor = len(nova)
print(lista[menor -1])
print(sum(lista) / len(lista))

