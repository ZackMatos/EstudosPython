
soma_mulheres = 0
homens_maiores = 0
mulheres = 0
while True:
      sexo = input("Digite seu sexo [M/F]:")
      idade = int(input("Digite sua idade:"))
      if idade < 0:
         break
      else:
           if sexo.upper() == "M" and idade >= 18:
                homens_maiores += 1
           if sexo.upper() == "F":
              mulheres += 1
              soma_mulheres += idade
           else:
               print("Opção inválida")
if mulheres > 0:
 media = soma_mulheres / mulheres
print("Há {} homens maiores de idade".format(homens_maiores))
if mulheres == 1:
    print("A média de idade de uma mulher é de {:.2f}".format(media))
else:
 print("A média de idade das {} mulheres é de {:.2f} anos".format(mulheres,media))