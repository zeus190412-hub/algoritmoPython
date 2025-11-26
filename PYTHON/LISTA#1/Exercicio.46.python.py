n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o sefgundo numero: "))
if n1 > n2:
    n1 , n2 = n2, n1

soma = 0

for i in range(n1, n2 + 1):
    if i % 2 != 0:
        soma += i

print(f"A soma dos numero impares entre {n1} e {n2} é: {soma}") 