velocidade_car = int(input('Digite a velocidade do carro: '))

if velocidade_car <= 80:
    print('Parabéns, você está no limite.')
else:
    multa = (velocidade_car-80)*7
    print('Infelizmente você será multado pela alta velocidade, custará R${:.2f}, porfavor conduza com cuidado.'.format(multa))
