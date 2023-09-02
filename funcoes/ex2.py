
def Positivo(numero: float) -> str:
    if numero <= 0:
        return 'N'
    else:
        return 'P'
    
print(Positivo(float(input('Numero: '))))