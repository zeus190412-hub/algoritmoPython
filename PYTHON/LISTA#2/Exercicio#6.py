turno = input("Digite o turno em que vocé estuda (M / V / N): ").upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor Invalido!")