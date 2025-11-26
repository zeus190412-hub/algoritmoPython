n1 = float(input("Digite a prova da primeira prova: "))
n2 = float(input("Digite a prova da segunda prova: "))
n3 = float(input("Digite a prova da terceira prova: "))
media = (n1*1 + n2*1 + n3*2) / 4
print(f"Media final : {media: .2f}")
if media >= 60:
    print("Aluno Aprovado!! ")
else:
    print("aluno reprovado!! ")