import random
j1 = str(input("\nEscreva o nome de um jogador de futebol: "))
j2 = str(input("Escreva o nome do segundo jogador de futebol: "))
j3 = str(input("Escreva o nome do terceiro jogador de futebol: "))

jogadores = [j1,j2,j3]
escolha_jogador = random.choice(jogadores)
print("\nO jogador: {} com certeza vai fazer um gol".format(escolha_jogador))

