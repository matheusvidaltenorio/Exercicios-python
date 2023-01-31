from math import cos, tan, sin, radians

angulo = float(input('Digite o valor do angulo: '))

seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O angulo {}, tem o Seno de {:.2f}'.format(angulo, seno))
print('O angulo {}, tem o Cosseno de {:.2f}'.format(angulo, cos))
print('O angulo {}, tem o Tangente de {:.2f}'.format(angulo, tan))
