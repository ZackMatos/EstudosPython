from exceptions import exceptions_int
tabuada = exceptions_int("Escolha um número para ver sua tabuada: ")
for x in range(1,11):
    print("{} x {} = {}".format(tabuada,x,tabuada*x))