area = float(input("Digite a area a ser pintada (em m2): "))
rendimento = float(input("Digite o rendimento da tinta (m2 por litro): "))
litros_por_lata = float(input("Digite quantos litros tem uma lata de tinta: "))
litros_necesarios = area / rendimento
import math
latas_necesarias = math.ceil(litros_necesarios / litros_por_lata)
print (f"Serão necesarias {latas_necesarias} lata(s) de tinta. ")