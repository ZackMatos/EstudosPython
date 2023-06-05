def exceptions_int(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError,TypeError):
            print ("\033[31mVocê não digitou um número inteiro, tente novamente...\033[m")
            continue
        else:
            return x

def exceptions_str(msg):
    while True:
        try:
            x = str(input(msg))
        except (ValueError,TypeError):
            print("\033[31mEntrada de dados inválida, tente novamente...\033[m")
            continue
        else:
            return x