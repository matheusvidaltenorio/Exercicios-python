#entrada de dados
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
#formula imc(indice massa corpórea)
imc = peso/(altura**2)

#entrando nas condições de cada peso
if imc < 18.5:
    print("Abaixo do peso adequado.Você está com {:.1f}".format(imc))
elif imc >= 18.5 and imc < 25.0:
    print("Você está no PESO IDEAL.Você está com {:.1f}".format(imc))
elif imc >= 25.0 and imc < 30.0:
    print("SOBREPESO.Você está com {:.1f}".format(imc))
elif imc >= 30.0 and imc < 40:
    print("OBESIDADE. Você está com {:.1f}".format(imc))
else:
    print("OBESIDADE MÓRBIDA.Você está com {:.1f}".format(imc))
