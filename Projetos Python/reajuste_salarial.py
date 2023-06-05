salario = float(input("Qual o salário do funcionário? R$"))
print("O salário de R${} com um aumento de 15%, passa a receber:R${:.2f}".format(salario,salario + (salario * 0.15)))