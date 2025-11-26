vendas = float(input("Digite o valor das vendas: "))
if vendas >= 100000:
    porcentagem = vendas * 0.16
    comissao = 700 + porcentagem
    print("COMISSAO: ", comissao)
elif vendas < 100000 and vendas >= 80000:
     porcentagem = vendas * 0.14
     comissao = 650 + porcentagem
     print("COMISSAO: ", comissao)
elif vendas < 80000 and vendas >= 60000:
     porcentagem = vendas * 0.12
     comissao = 600 + porcentagem
     print("COMISSAO: ", comissao)
elif vendas < 60000 and vendas >= 40000:
     porcentagem = vendas * 0.10
     comissao = 550 + porcentagem
     print("COMISSAO: ", comissao)
elif vendas < 40000 and vendas >= 20000:
     porcentagem = vendas * 0.8
     comissao = 500 + porcentagem
     print("COMISSAO: ", comissao)
else:
     vendas < 20000
     porcentagem = vendas * 0.6
     comissao = 400 + porcentagem
     print("COMISSAO: ", comissao)