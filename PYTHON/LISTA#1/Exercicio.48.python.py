consumo = float(input("Digite o consumo de enrgia (kWh): "))
preço_kwh = float(input("Digite o preço por kWh (R$): "))
valor_conta = consumo * preço_kwh
print(f"Valor da conta de luz: R$ {valor_conta:.2f}")