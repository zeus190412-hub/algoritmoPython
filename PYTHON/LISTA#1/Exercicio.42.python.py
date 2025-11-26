mensalidade = float(input("Digite o valor actual da mensalidade: R$ "))
percentual = float(input("Digite o percentual de aumento (%): "))
aumento = mensalidade * (percentual / 100)
novo_valor = mensalidade + aumento
print(f"Novo valor da mensalidade: R$ {novo_valor:.2f}")