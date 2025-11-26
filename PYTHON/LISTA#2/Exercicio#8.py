import math
numero = float(input("Digite um numero: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada é: {raiz}")
else:
    print("Numero Invalido!")