import time
cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        cont+=1
        #time.sleep()
print('A soma de todos os números solicitados {} multiplos de 3 são {} '.format(cont, soma))
