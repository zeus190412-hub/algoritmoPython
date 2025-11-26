print(" CALCULATOR 544 ")
print("1 - Soma de 2 numeros")
print("2 - Diferença de 2 numeros")
print("3 - Producto entre 2 numeros")
print("4 - Divisão entre 2 numeros")

op = int(input("Escolha a opcão 1 - 2 - 3 ou 4: "))
n1 = float(input("Digite N1: "))
n2 = float(input("Digite N2: "))

if op == 1:
    res = n1 + n2
    print(res)
elif op == 2:
    res = n1 - n2
    print(res)
elif op == 3:
    res = n1 * n2
    print(res)
elif op == 4:
    if n1 == 0:
        print("Denominador não pode ser ZERO!! ")
    else:
        print(n1/n2)
else:
    print("opção invalida")

