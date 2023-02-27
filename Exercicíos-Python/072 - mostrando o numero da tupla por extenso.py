numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 0 a 20: '))
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num <= 20:
        if num >= 0:
            print(f'{numeros[num]} por extenso é o numero digitado que é {num}')
            break
