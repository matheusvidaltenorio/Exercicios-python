#ENTRADA DE DADOS DOS LADOS DO TRIANGULO
lado1 = int(input("Digite um lado do triangulo: "))
lado2 = int(input("Digite outro lado do triangulo:  "))
lado3 = int(input("Digite outro lado do triangulo: "))
#ACONTECERÁ A COMPARAÇÃO DOS LADOS
if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado3+lado2 > lado1:
    print("Pode formar um triangulo.")
    if lado1 == lado2 == lado3:
             print("TRIANGULO DO TIPO: EQUILÁTERO")
    if lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado2==lado3!=lado1:
             print("TRIANGULO DO TIPO: ISÓSCELES")
    if lado1 != lado2 != lado3 != lado1:
             print("TRIANGULO DO TIPO: ESCALENO")

else:
    print("Não pode formar um triângulo.")

