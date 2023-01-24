nome = input('Digite seu nome: ')
salario_antigo = int(input('Digite seu salário: '))
salario_final = salario_antigo+(salario_antigo*(15/100))
print('O funcionário {}, que ganhava {}, agora irá ganhar {}'.format(nome, salario_antigo, salario_final))