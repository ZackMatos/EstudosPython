from exceptions import exceptions_float
peso = exceptions_float("Qual seu peso? (Kg) ")
altura = exceptions_float("Qual sua altura? (m) ")
while peso <= 0 or altura <= 0:
     print("Informação inválida, tente novamente")
     peso = exceptions_float("Qual seu peso? (Kg) ")
     altura = exceptions_float("Qual sua altura? (m) ")
imc = peso / (altura**2)

print("O seu IMC é de {:.1f}".format(imc))
if imc <= 18.49:
    print("Você tem que se alimentar melhor")
elif imc <= 24.99:
    print("Você está na faixa de PESO IDEAL")
elif imc <=29.99:
    print("Você está na faixa de SOBREPESO")
else:
    print("Você está na faixa de OBESIDADE")