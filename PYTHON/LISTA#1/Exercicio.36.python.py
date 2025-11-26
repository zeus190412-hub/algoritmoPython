area_piso = float(input("Digite a area do piso (m²): "))
area_azulejo = float(input("Digite a area de cada azulejo (m²): "))
quantidade = area_piso / area_azulejo
print(f"quantidade necessaria de azulejos: {quantidade:.0f}")