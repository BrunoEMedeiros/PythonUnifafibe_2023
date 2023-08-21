salario_hr = float(input('Valor hr: '))
hrs_mes = float(input('Horas trabalhadas no mês: '))

salario = (((salario_hr * 8) * 5) * 4)

if hrs_mes <= 160:
    print('Seu salario é:', salario)
else:
    salario += ((salario_hr * 1.5) * (hrs_mes - 160))
    print(salario)