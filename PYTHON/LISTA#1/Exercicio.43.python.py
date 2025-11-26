capital = float(input("Digite o capital inicial: R$ "))
taxa = float(input("Digite a taxa de juros (% ao periodo): "))
tempo = int(input("Digite o tempo (numero de periodos): "))
i = taxa / 100
montante = capital * (1 + i) ** tempo
print(f"Montante final: R$ {montante:.2f}")