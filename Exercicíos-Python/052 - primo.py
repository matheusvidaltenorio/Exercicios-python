num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num+1, 1):
    if num % c == 0:
        print('{', c, "}")
        cont = cont + 1
    else:
        print(c)
if cont == 2:
    print('É por isso que ele é PRIMO.')
else:
    print('É pór isso que el não é PRIMO')
print('O número primo {} foi divisível {} vezes'.format(num , cont))