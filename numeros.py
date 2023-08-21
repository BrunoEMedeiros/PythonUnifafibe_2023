a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))

maior = 0
menor = 0

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

print('Maior:', maior)
print('Menor:', menor)
print('Media:',((a + b+ c) / 3))