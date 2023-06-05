def excecoes_int(msg): 
    while True:
     try:
        x = int(input(msg))
     except (ValueError,TypeError):
        print("\nEntrada de dados inválida... tente novamente\n")
        continue
     else:
        return x

def excecoes_float(msg):
   while True:
      try:
         x = float(input(msg))
      except (ValueError,TypeError):
          print("\nEntrada de dados inválida... tente novamente\n")
          continue
      else:
        return x