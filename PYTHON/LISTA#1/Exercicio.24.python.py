preço_custo = float(input("Digite o preço de custo do producto: "))
preço_venda = float(input("Digite o preço de venda do producto: "))
lucro = preço_venda - preço_custo
lucro_percentual = (lucro / preço_custo) * 100
print(f"lucro: R$ {lucro:.2f}")
print(f"lucro percentual: {lucro_percentual:.2f}%")