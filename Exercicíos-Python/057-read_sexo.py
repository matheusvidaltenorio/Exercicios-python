sexo = str(input('Digite seu sexo: [F/M]')).upper()
while sexo != 'F' and sexo != 'M':
            print('Sexo errado, você digitou {}, porfavor DIGITE SEU SEXO NOVAMENTE.'.format(sexo))
            sexo = str(input('Digite seu sexo: [F/M]')).upper()

print('Você printou o sexo correto, que foi um dos dois MASCULINO(M) OU (F)FEMININO {}.'.format(sexo))
