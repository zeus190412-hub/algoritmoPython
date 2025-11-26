distancia = float(input("informe a distancia da viagem em (km): "))
comsumo = float(input("informe o consumo do carro (km por litro): "))
preço = float(input("informe o preço do combustivel (por litro): "))
litros = distancia / comsumo
custo = litros * preço
print("Custo estimado da viagem: R$", round(custo, 2))