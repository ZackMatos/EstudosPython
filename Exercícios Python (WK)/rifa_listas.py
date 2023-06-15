''' Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua cerimônia de formatura. Construa um programa para cadastrar os nomes das pessoas que compraram a rifa. Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.'''

#Minha resolução
from random import shuffle 
from random import choice
rifa = []
while True:
    nomes = input("\nDigite o nome da pessoa que vai participar da rifa:")
    rifa.append(nomes)
    continuar = input("Deseja colocar mais nomes na rifa? S/N:")
    if continuar.upper() == "N":
        break
shuffle(rifa) #embaralhando os nomes
sorteado = choice(rifa)
print("\n\033[33mPARABÉNS\033[m {}, agora você já pode pegar o prêmio!!!".format(sorteado))

