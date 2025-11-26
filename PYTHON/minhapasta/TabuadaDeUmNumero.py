numero = int(input("Digite um numero para ver a tabuada: "))
print("tabuada do ", numero)
for i in range(1, 11):
    print(numero, "*", i,"=", numero * i)