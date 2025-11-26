salario = float(input ("Digite o salario actual (R$): "))
aumneto = float(input("Digite o percentual de aumneto (%):"))
novo_salario = salario + (salario * aumneto / 100)
print("O novo salario é de ", novo_salario, "R$" )