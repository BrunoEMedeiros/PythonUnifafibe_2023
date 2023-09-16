try:
  # Código que pode gerar uma exceção
  x = int(input("Digite um número inteiro: "))
except ValueError:
  # Tratamento da exceção
  print("O valor não é um número inteiro")
else:
  # Código executado se nenhuma exceção for lançada
  print(f"O valor digitado é {x}")

