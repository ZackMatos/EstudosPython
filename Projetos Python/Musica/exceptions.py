def exceptions_int(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError,TypeError):
            print("\033[31mEntrada de dados inválida, tente novamente...\033[m")
            continue
        else:
            return x