equipamentos = []
preço_equipamentos = []
while True: #Loop infinito (por isso a necessidade de um break)
    adicionar_equipamento = input("\nQual o nome do equipamento? ")
    equipamentos.append(adicionar_equipamento)
    preço = float(input("Qual o preço do equipamento? "))
    preço_equipamentos.append(preço)
    continuar = input("Deseja adicionar mais equipamentos? S/N: ")
    if continuar.upper() == "N":
        break
print(equipamentos)
print(preço_equipamentos)

indice_mais_barato = preço_equipamentos.index(min(preço_equipamentos))
indice_mais_caro = preço_equipamentos.index(max(preço_equipamentos))

preco_mais_barato = (min(preço_equipamentos))
preco_mais_caro = (max(preço_equipamentos))
media = sum(preço_equipamentos) / len(preço_equipamentos)

print("\nO equipamento mais barato é: {} com o preço de R${:.2f}".format(equipamentos[indice_mais_barato],preco_mais_barato))

print("O equipamento mais caro é: {} com o preço de R${:.2f}".format(equipamentos[indice_mais_caro],preco_mais_caro))

print("\nA média de preço dos equipamentos são de: R${:.2f}".format(media))
    