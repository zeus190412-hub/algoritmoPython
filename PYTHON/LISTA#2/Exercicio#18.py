sexo = input("Digite o sexo (M para masculino, F para femenino): ").upper()
altura = float(input("Digite a altura (em metros): "))
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para homem: {peso_ideal:.2f} kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal para mulher:{peso_ideal:.2f} kg")
else:
    print("Sexo Invalido!! Digite apenas M ou F. ")