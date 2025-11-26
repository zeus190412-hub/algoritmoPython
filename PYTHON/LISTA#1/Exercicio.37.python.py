valor = float(input("Digite o valor do produto: R$ "))
taxa_imposto = float(input("Digite a taxa do imposto (%): "))
imposto = valor * (taxa_imposto / 100)
valor_final = valor + imposto
print(f"Imposto: R$ {imposto:.2f}")
print(f"Valor final do produto: R$ {valor_final:.2f}")