from datetime import date
from exceptions import excecoes_int
data = date.today().year
ano_nascimento = excecoes_int("Digite seu ano de nascimento: ")
idade = data - ano_nascimento
if idade > 0 and idade < 110:
 print("O atleta tem {} anos".format(idade))
while idade <= 0 or idade > 109:
      print("Talvez você tenha se confundido, tente novamente")
      ano_nascimento = int(input("Digite seu ano de nascimento: "))
      idade = data - ano_nascimento
      if idade > 0 and idade <109:
       print("O atleta tem {} anos".format(idade))


if idade <= 9:
    classificacao = "MIRIM"
elif idade <= 14:
    classificacao = "INFANTIL"
elif idade <=19:
    classificacao = "JUNIOR"
elif idade <=25:
    classificacao = "Sênior"
else:
    classificacao = "MESTRE"
print("Sua classificação é {}".format(classificacao))