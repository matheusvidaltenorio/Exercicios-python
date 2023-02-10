#IMPORTANDO A BIBLIOTECA DATETIME PARA PEGAR O ANO ATUAL
from datetime import date
ano = date.today().year
#ENTRADA DO ANO DO CLIENTE
ano_nas = int(input("Digite seu ano de nascimento: "))
idade = ano - ano_nas

#COMPARAÇÃO DO RESULTADO DA IDADE COM AS IDADES DESEJADAS POR CADA CATEGORIA
if idade <= 9:
    print("CATEGORIA : MIRIM.")
elif idade <= 14:
    print("CATEGORIA : INFANTIL.")
elif  idade <= 19:
    print("CATEGORIA : JUNIOR.")
elif idade <= 25:
    print("CATEGORIA : SENIOR.")
else:
    print("CATEGORIA : MASTER.")

