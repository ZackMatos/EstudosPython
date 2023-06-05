def excecoes(msg): #Função para não permitir que o usuário digite dados inválidos
    while True:
     try:
        x = int(input(msg))
     except (ValueError,TypeError):
        print("\nEntrada de dados inválida... tente novamente\n")
        continue
     else:
        return x
