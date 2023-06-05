import moeda #Aprendendo a importar módulos  
preco = moeda.exceptions_float("Digite o preço: R$")
aumento = moeda.exceptions_int("Digite a porcentagem:")
print(moeda.metade(preco))
print(moeda.dobro(preco))
print(moeda.aumentar(aumento,preco))
print(moeda.diminuir(aumento,preco))