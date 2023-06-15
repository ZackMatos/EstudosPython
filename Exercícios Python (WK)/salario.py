profissao = input("Digite sua profissão: ")
salario = float(input("Digite seu salário:"))
if profissao == "Programador":
     print("Seu novo salário como {} será de R${}".format(profissao,salario * 1.50))
elif profissao == "Analista de Sistemas":
     print("Seu novo salário como {} será de R${}".format(profissao,salario * 1.40))
elif profissao == "Analista de banco de dados":
     print("Seu novo salário como {} será de R${}".format(profissao,salario * 1.30))
else:
     print("Cargo inválido")