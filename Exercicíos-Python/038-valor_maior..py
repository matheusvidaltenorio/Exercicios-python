n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

if n1 > n2:
    print("{} é o valor maior".format(n1))
elif n2 > n1:
    print("{} é o valor maior".format(n2))
else:
    print("Não existe valor maior, ambos são iguais.")
