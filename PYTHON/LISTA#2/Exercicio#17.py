salario = float(input("Digite o seu salario: R$ "))
prestação = float(input("Digite o valor da prestação do emprestimo: R$"))
limite = salario * 0.20
if prestação > limite:
    print("Emprestamo não concedido.")
else:
    print("Emprestamo concedido ")