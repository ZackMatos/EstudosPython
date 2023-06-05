from random import randint
from time import sleep
from exceptions import excecoes_int
 
print("VAMOS JOGAR JOKENPO? ")
print("S - SIM\nN - NÃO\n")
escolha = str(input("Escolha uma opção: "))
escolha = escolha.lower()

while escolha != "s" and escolha != "n":
      print("\nNão entendi... digite novamente, por favor\n")
      escolha = str(input("Escolha uma opção: "))

if escolha == "n":
  print("Tchau...")
  quit()



if escolha == "s":   
    print("ESCOLHAS:")
    print("\n0-Pedra\n1-Papel\n2-Tesoura\n")
    opcoes = ["Pedra","Papel","Tesoura"]

    jogada = excecoes_int("Qual jogada você vai fazer? ")
    computador_jogadas = randint(0,2)
    
    
    while jogada == computador_jogadas:
        print("Você escolheu {}".format(opcoes[jogada]))
        print("O Computador escolheu {}".format(opcoes[computador_jogadas]))
        print("\nOPA, DEU EMPATE!!!, vamos tentar de novo\n")
        jogada = excecoes_int("Qual jogada você vai fazer? ")
        computador_jogadas = randint(0,2)
        if jogada != 1 and jogada != 0 and jogada != 2:
           print("\nJogada inválida, tente novamente\n")
           jogada = excecoes_int("Qual jogada você vai fazer? ")
           computador_jogadas = randint(0,2)

    while jogada != 1 and jogada != 0 and jogada!= 2:
            print("\nJogada inválida, tente novamente\n")
            jogada = excecoes_int("Qual jogada você vai fazer? ")
            computador_jogadas = randint(0,2)

    print("JO")
    sleep(2)
    print("KEN")
    sleep(2)
    print("PO!!!\n")    
    print("Você escolheu {}".format(opcoes[jogada]))
    print("O computador escolheu {}".format(opcoes[computador_jogadas]))
   


    if jogada == 0 and computador_jogadas == 1: #Computador - Papel
     print("\nCOMPUTADOR VENCE!!!")
     pontos_computador = 1

    elif jogada == 1 and computador_jogadas == 2: #Computador - Tesoura
     print("\nCOMPUTADOR VENCEU!!!\n")
     pontos_computador = 1

    elif jogada == 2 and computador_jogadas == 0: #Computador - Pedra
     print("\nCOMPUTADOR VENCEU!!!\n")
     pontos_computador = 1
    

    
    else:
     print("\nVOCÊ VENCEU!!!\n")
     pontos_jogador = 1










