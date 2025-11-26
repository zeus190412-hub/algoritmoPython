preço_aquisição = float(input("Digite o valor da aquisição do produto: R$ "))
if preço_aquisição < 50:
    preço_venda = preço_aquisição * 1.45
else:
    preço_venda = preço_aquisição * 1.30
print(f"Valor de venda:R$ {preço_venda: .2f}")