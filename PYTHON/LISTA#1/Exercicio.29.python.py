saque = int(input("Digite o valor do saque (em reais): "))
cedulas_100 = saque // 100
resto = saque % 100
cedulas_50 = saque // 50
resto = saque % 50
cedulas_20 = saque // 20
resto = saque % 20
cedulas_10 = saque // 10
resto = saque % 10
cedulas_5 = saque // 5
resto = saque % 5
cedulas_2 = saque // 2
resto = saque % 2
print("Cedulas necessarias: ")
print(f"R$100: {cedulas_100}")
print(f"R$50: {cedulas_50}")
print(f"R$20: {cedulas_20}")
print(f"R$10: {cedulas_10}")
print(f"R$5: {cedulas_5}")
print(f"R$2: {cedulas_2}")
if resto != 0:
    print(f"Valor restante que não pode ser sacado: R${resto}")
