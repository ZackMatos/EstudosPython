import exceptions
dias = exceptions.excecoes_int("Quantos dias alugados? ")
km = exceptions.excecoes_float("Quantos kilômetros rodados? ")
print("O total a pagar é:{:.2f}".format((60*dias) + (0.15 * km)))