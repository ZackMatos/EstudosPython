from exceptions import excecoes_float
preco = excecoes_float("Qual o preço do produto? R$")
print("O produto que custava R${:.2f}, na promoção com  um desconto de 5% irá custar R${:.2f}".format(preco,preco - (0.05 * preco)))
