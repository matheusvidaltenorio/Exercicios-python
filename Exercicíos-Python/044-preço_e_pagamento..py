valor_prod = float(input("Digite o valor do produto:R$"))
opc_pag = int(input("Digite sua opção de pagamento:\n1 - À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO.\n2 - À VISTA NO CARTÃO: 5% DE DESCONTO."
                           "\n3 - EM ATÉ 2X NO CARTÃO : PREÇO NORMAL.\n4 - 3X OU MAIS NO CARTÃO : 20% DE JUROS.\nDigite sua opção: "))

if opc_pag == 1:
    cal = valor_prod-(valor_prod*10/100)
    print("Você escolheu o modo À VISTA, terá 10% de desconto, O preço é {:.2f}, e ficará por {:.2f}".format(valor_prod, cal))
elif opc_pag == 2:
    cal = valor_prod-(valor_prod*5/100)
    print("Você escolheu o modo À VISTA PORÉM NO CARTÃO, terá 5% de desconto, O preço é {:.2f}, e ficará por {:.2f}".format(valor_prod, cal))
elif opc_pag == 3:
    cal = valor_prod
    print("Você escolheu o modo CARTÃO EM ATÉ 2X, terá 10% de desconto, O preço é {:.2f}, e ficará por {:.2f}".format(valor_prod, cal))
elif opc_pag == 4:
    parcelas = int(input("Quantas parcelas serão? "))
    cal = valor_prod + (valor_prod * 20 / 100)
    print('Você escolheu o modo CARTÃO E QUIS DIVIDIR EM {:.2f}x de R${:.2f} , O preço é {:.2f}, e ficará por {:.2f}'.format(parcelas, (cal / parcelas), valor_prod, cal))
else:
    print("Erro de código, porfavor informe novamente a forma de opção..")