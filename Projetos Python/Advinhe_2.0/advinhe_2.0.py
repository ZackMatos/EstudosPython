from random import randint
from time import sleep
from exceptions import excecoes
tentativas = 0
print("\033[33mEstou pensando em um número...\033[m\n")
sleep(2)
computador = randint(0,10)
print("Pronto, já pensei, é um número \033[34mentre 0 e 10\033[m\n")
escolha = excecoes("Em que número estou pensando? ")

while escolha !=computador:
 tentativas+= 1
 if escolha < computador:
    print("Opa, é um número \033[33mMAIOR\033[m que {}\n".format(escolha))
    escolha = excecoes("Em que número estou pensando? ")
 else:
   print("É um número \033[33mMENOR\033[m que {}\n".format(escolha))
   escolha = excecoes("Em que número estou pensando? ")
if escolha == computador:
   tentativas+=1
   if tentativas == 1:
    print("\n\033[32mPARABÉNS, VOCÊ ACERTOU COM {} TENTATIVA!!!\033[m".format(tentativas))
   else:
     print("\n\033[32mPARABÉNS, VOCÊ ACERTOU COM {} TENTATIVAS!!!\033[m".format(tentativas))
