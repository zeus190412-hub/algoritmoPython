n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
if (n1 < 0 or n1 > 10) or (n2 <0 or n2 < 10):
    print("Nota invalida! o programa sera encerrado. ")
else:
    media = (n1 + n2) / 2
    print(f"Amedia das notas é: {media} ")