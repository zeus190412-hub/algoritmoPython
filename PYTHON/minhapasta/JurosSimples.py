capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa de juros ao mes (%): "))
tempo = float(input("Digite o tempo em meses: "))
taxa = taxa / 100
montante = capital + (capital * taxa * tempo)
print("O montante final é de R$ ", montante)