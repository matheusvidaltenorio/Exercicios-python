from datetime import date
#ENTRADA DE DADOS
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
genero = int(input("1 - HOMEM\n2 - MULHER.\nDigite seu o número do seu genêro: "))
ano = date.today().year
idade = ano - ano_nascimento
#COLOCANDO OS DADOS PARA SE COMPARAREM COM OUTROS DADOS INFORMADOS.
# FOI COLOCADO SOMENTE A IDADE E ALISTAMENTO, PORÉM FOI COLOCADO POR CURIOSIDADE E ESTUDO O GENERO.#
if idade < 18 and genero == 1:
    print("Você é do Sexo Masculino.\nVocê tem o DEVER de se ALISTAR. Você ainda vai se alistar ao serviço militar, você só tem {}, falta {}, "
          "o ano de alistamento será em {}".format(idade, (idade-18), (ano_nascimento+18)))


elif idade < 18 and genero == 2:
    print("Você NÃO PRECISA SE ALISTAR, POIS É DO SEXO FEMININO. Mas se quisesse Você ainda não poderia se alistar ao serviço militar, você só tem {}, falta {}, "
          "o ano de alistamento será em {}".format(idade, (idade-18), (ano_nascimento+18)))


elif idade == 18 and genero == 1:
    print("Você é do Sexo Masculino.\nVocê tem {} anos em {} e já deve se ALISTAR IMEDIATAMENTE.".format(idade, (ano_nascimento+18)))


elif idade == 18 and genero == 2:
    print("Você não tem OBRIGAÇÃO POIS É DO SEXO FEMININO. Mas se quisesse, já estaria APTA pela IDADe. Pois Você tem {} anos em {}.".format(idade, (ano_nascimento+18)))


elif idade > 18 and genero == 1:
    print("Você é do Sexo Masculino,OK.\nJá passou do tempo, você já tem idade de {} anos , e já se passaram {} ano(s), seu alistamento foi em {} busque um quartel maix próximo para mais "
          "informações.".format(idade, (idade-18), (ano - (idade-18))))

else:
    print("Você é do Sexo Feminino,NÃO TEM O DEVER.\nMas se quisesse,Já passou do tempo, você já tem idade de {} anos , e já se passaram {} ano(s), seu alistamento foi em {} busque um quartel maix próximo para mais "
        "informações.".format(idade, (idade - 18), (ano - (idade - 18))))

