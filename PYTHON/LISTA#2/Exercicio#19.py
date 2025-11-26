numero = int(input("Digite um numero inteiro maior que zero: "))
if numero <=0:
    print("Numero Invalido")
else:
    soma = 0
    for algarismo in str(numero):
        soma +=int(algarismo)
    print("A soma dos algorismo é:", soma)