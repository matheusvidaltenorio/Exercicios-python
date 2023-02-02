num = int(input('Digite um ano qualquer: '))


if num%4==0 and num%100!=0 or num%400==0:
    print('O ano digitado é bissexto, {}.'.format(num))
else:
    print('Não são bissexto.')