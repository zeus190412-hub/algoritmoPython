n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero:"))
if n1 > n2:
    maior = n1
    diferença = n1 - n2
else:
    maior = n2
    diferença = n2 - n1
print("O maior numero é: ", maior)
print("A diferença entre eles é:", diferença)