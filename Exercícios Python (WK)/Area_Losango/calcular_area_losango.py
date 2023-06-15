from func_calcular_area_losango import calcular_area_losango
diagonal_maior = int(input("Digite um valor para a diagonal maior do Losângulo:"))
diagonal_menor = int(input("Digite um valor para a diagonal menor do Losângulo:"))
print("\nA área desse Losângulo é de: {:.0f}cm²\n".format(calcular_area_losango(diagonal_maior,diagonal_menor)))
