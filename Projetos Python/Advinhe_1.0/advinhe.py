from random import randint
from time import sleep
from exceptions import excecoes
chances = 1
numero = randint(0, 10)
print("Estou pensando em um número \033[34mentre 0 e 10\033[m\n")
print("\033[33mPensando...\033[m\n")
sleep(2)
print("Pronto já pensei, tenta a sorte!\n")
#Testando se o código funciona quando a pessoa acerta
#print("Eu pensei no número {}".format(numero))
resposta = excecoes("Em que número eu pensei? ")


while (chances == 1 and resposta >= 10 or chances ==1 and resposta <= 0):
       print("\nNão não... é um número entre 0 e 10, vou te dar mais uma chance")
       print("Já pensei em outro número\n")
       resposta = excecoes("Em que número eu estou pensando? ")
       chances -= 1
       

if (chances == 0 and resposta >= 10 or resposta <= 0):
  print("\nDesisto, você não entendeu a brincadeira")

if (resposta < 10 and resposta > 0):      
    print("\033[33mANALISANDO SUA RESPOSTA...\033[m\n")
    sleep(3)
    print("\033[33mFAZENDO CÁLCULOS SUPER COMPLEXOS...\033[m\n")
    sleep(2)
    if (resposta == numero):
     print("\033[32mVOCÊ ACERTOU!\033[m, eu pensei no número {}".format(numero))
    else:
     print("\033[31mVOCÊ ERROU!\033[m, eu pensei no número {} e não no número {}".format(numero, resposta))


