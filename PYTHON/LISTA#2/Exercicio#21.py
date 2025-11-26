trab = float(input("Digite o valor do trabalho: "))
ava = float(input("Digite o valor do avaliação: "))
exa = float(input("Digite o valor do exame: "))

if (trab < 0 or trab > 10) or (ava < 0 or ava > 10) or (exa < 0 or exa > 10):
    print("Nota invalida!! ")
else:
    media = ((trab * 2) +  (ava * 3) +  (exa * 5)) / 10
    print(media)
    if media >= 0 and media <= 2.99:
        print("REPROVADO, Media: ", media)
    elif media >= 3 and media <= 5.99:
        print("EXAME, Media: ", media)
    else:
        print("APROVADO, Media: ", media)