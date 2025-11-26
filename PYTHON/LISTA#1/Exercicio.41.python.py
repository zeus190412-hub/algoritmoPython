a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
resultado = 0
for _ in range(b):
    resultado += a
    print(f"O resultado da multiplicação é: {resultado}")