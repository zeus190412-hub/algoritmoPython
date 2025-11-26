segundos = int(input("digite o valor em segundos:"))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60
print(f"{horas} hora(s), {minutos} minutos(s) e {segundos_restantes} segundos(s) ")