tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))
tamanho_megabits = tamanho_mb * 8 
tempo_segundos = tamanho_megabits / velocidade_mbps
print (f"Tempo estimado de download:{tempo_segundos:.2f} segundos") 