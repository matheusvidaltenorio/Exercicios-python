valor_casa = int(input("Qual é o valor da casa? "))
salario_comprador = int(input("Quanto é que você ganha? "))
tempo = int(input("Quantas anos você irá pagar? "))

valor_parcela = valor_casa/(tempo*12)

print("Para pagar uma casa de {} em {} anos a prestação será de {:.2f}".format(valor_casa, tempo, valor_parcela))
if (salario_comprador*(30/100) > valor_parcela):
    print("Empréstimo ACEITO.")
else:
    print("Infelizmente você não poderá comprar a casa, Empréstimo NEGADO.")