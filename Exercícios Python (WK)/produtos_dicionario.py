produtos = {}
while True:
    codigo = int(input("\nDigite o código do produto:"))
    nome = input("Digite o nome do produto:")
    preco = float(input("Digite o preço do produto:"))
    qntd = int(input("Digite a quantidade:"))
    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(qntd)
    produtos.update({codigo:prod})
    continuar = input("Deseja continuar? S/N:")
    if continuar.upper() == "N":
        break
total = 0
for x in sorted(produtos.values()):
    subtotal = x[1] * x[2]
    print("{}: R${:.2f}".format(x[0],subtotal))
    total += subtotal
print("\nTotal: R${:.2f}".format(total))
