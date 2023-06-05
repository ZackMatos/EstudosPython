def exceptions_str(msg):
    while True:
        try:
            x = str(input(msg))
        except:
            print("\033[31mEntrada de dados inválida, tente novamente...\033[m")
            continue
        else:
            return x