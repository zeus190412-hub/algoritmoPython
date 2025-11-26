nome = input("Qual é seu nome: ")
print("seu nome é: ", nome)

disciplina = input("Digite o nome da sua disciplina: ")
print("seu nome é: ", disciplina)

nota1 = float(input("Digite a primeira nota: "))
print("sua primeira nota é: ", nota1)

nota2 = float(input("Digite a segunda nota: "))
print("sua segunda nota é: ", nota2)

nota3 = float(input("Digite a terceira nota: "))
print("sua terceira nota é: ", nota3)

media = (nota1 + nota2 + nota3) / 3
print("Sua media é:", media)

if media >= 6.0:
    situação = "APROVADO!!"
else:
    situação = "REPROVADO!!!!"
    print("Situação: ", situação)