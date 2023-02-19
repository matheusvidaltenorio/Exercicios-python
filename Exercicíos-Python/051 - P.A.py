#MINHA FORMA DE FAZER
import time
print('='*20, '10 TERMOS DE UMA P.A', '='*20)
termo_inicio = int(input('Digite o valor inicial: '))
razao = int(input('Digite a razao:  '))
pa = termo_inicio
for c in range(1, 11, 1):
    print(pa, '-> ', end=' ')
    pa = pa + razao
    time.sleep(0.5)
print('Acabou!')

#FORMA DO PROFESSOR
"""
import time
print('='*20, '10 TERMOS DE UMA P.A', '='*20)
termo_inicio = int(input('Digite o valor inicial: '))
razao = int(input('Digite a razao:  '))
decimo = termo_inicio + (10 - 1 )* razao

for c in range(termo_inicio, decimo, razao):
    print(c, '-> ', end=' ')
    time.sleep(0.5)
print('Acabou!')
"""