from exceptions import exceptions_int
tabuada = exceptions_int("Quer fazer a tabuada de qual valor? (Digite 0 para parar) ")
while tabuada != 0:
      for x in range(1,11):
          print("{} x {} = {}".format(tabuada,x,tabuada*x))
      if x == 10:
          tabuada = exceptions_int("Quer fazer a tabuada de qual valor? (Digite 0 para parar) ")
if tabuada == 0:
    quit()