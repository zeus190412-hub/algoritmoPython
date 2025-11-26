valor = float(input("Digite o valor do producto (R$): "))
desconto = float(input("Digote o porcentual de desconto (%): "))
valor_final = valor - (valor * desconto / 100)
print("O valor final com desconto é: ", valor_final , "R$")