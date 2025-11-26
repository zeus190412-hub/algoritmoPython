horas = float(input("Digite o numero de horas trabalhadas:"))
valor_hora = 40.50
salario_bruto = horas * valor_hora
if salario_bruto > 2500:
    imposto = salario_bruto * 0.11
else:
    imposto = 0
salario_liquido = salario_bruto - imposto
print(f"Salario bruto: R$ {salario_bruto:.2f}")
print(f"Imposto descontado: R$ {imposto:.2f}")
print(f"Salario liquido: R$ {salario_liquido:.2f}")