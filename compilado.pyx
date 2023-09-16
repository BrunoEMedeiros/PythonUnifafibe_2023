import time

inicio = time.time()

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("Sequência de Fibonacci:")
    for i in range(0, 30):
        print(fibonacci(i))

if __name__ == "__main__":
    main()

fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")


