reta1 = int(input('Digite o valor da reta: '))
reta2 = int(input('Digite o valor da reta: '))
reta3 = int(input('Digite o valor da reta: '))

if reta1+reta2 > reta3 or reta1+reta3 > reta2 or reta3+reta2 > reta1:
    print('Formará um triangulo.')
else:
    print('Não formará um triangulo.')


