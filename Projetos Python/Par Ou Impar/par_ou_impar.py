from random import randint
import exceptions
print("VAMOS JOGAR PAR OU IMPAR!!!")
valor = exceptions.exceptions_int("Digite um valor: ")
print("P - PAR OU I - IMPAR")
par_ou_impar = exceptions.exceptions_str("")
par_ou_impar = par_ou_impar.upper()
computador = randint(0,10)
if par_ou_impar == "P" or par_ou_impar == "I":
 print("Você escolheu {} e o Computador escolheu {}\n".format(valor,computador))
# if par_ou_impar == "P":
#    if (computador + valor) % 2 == 0:
#       print("BOA, VOCÊ VENCEU!!!")
#    else:
#       print("INFELIZMENTE VOCÊ PERDEU!!!")
# else:
#    if (computador + valor) % 2 != 0:
#       print("BOA, VOCÊ VENCEU!!!")
#    else:
#       print("INFELIZMENTE VOCÊ PERDEU!!!")


 
while par_ou_impar != "P" and par_ou_impar != "I":
            print("\033[31mESCOLHA INVÁLIDA, TENTE NOVAMENTE\033[m\n")
            print("VAMOS JOGAR PAR OU IMPAR!!!")
            valor = exceptions.exceptions_int("Digite um valor: ")
            print("P - PAR OU I - IMPAR")
            par_ou_impar = exceptions.exceptions_str("")
            par_ou_impar = par_ou_impar.upper()
            computador = randint(0,10)
            if par_ou_impar == "P" or par_ou_impar == "I":
             print("Você escolheu {} e o Computador escolheu {}\n".format(valor,computador))

match par_ou_impar:
    case "P":
       if (computador + valor) % 2 == 0:
           print("{} É PAR".format(computador + valor))
           print("BOA, VOCÊ VENCEU!!!")
       else:
          print("{} NÃO É PAR".format(computador + valor))
          print("INFELIZMENTE VOCÊ PERDEU!!!")
    case "I":
        if (computador + valor) % 2 != 0:
         print("{} É ÍMPAR".format(computador + valor))
         print("BOA, VOCÊ VENCEU!!!")
        else:
           print("{} NÃO É ÍMPAR".format(computador + valor))
           print("INFELIZMENTE VOCÊ PERDEU!!!")

        

    

