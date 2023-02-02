salario = float(input('Digite o quanto você ganha: R$'))


if salario > 1250:
    novo_sal = salario+(salario*10/100)
    print('O novo salario ficara: {}'.format(novo_sal))
else:
    novo_sal = salario+(salario*15/100)
    print('O novo salario ficara: {}'.format(novo_sal))


