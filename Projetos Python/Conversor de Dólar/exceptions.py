def exceptions_float(msg):
    while True:
        try:
          x = float(input(msg))
        except (ValueError,TypeError):
           print("Você não digitou um número, tente novamente...")
           continue
        else:
           return x