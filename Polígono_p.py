# Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
# Calcular e imprimir o seguinte:
# Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
# Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
# Se o número de lados for igual a 5 escrever PENTÁGONO.
# Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
# Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.


num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado em cm: "))

if num_lados < 3:
  print("NÃO É UM POLÍGONO")
elif num_lados == 3:
  area = (medida_lado ** 2 * (3 ** 0.5)) / 4  # fórmula da área do triângulo equilátero
  print("TRIÂNGULO, área:", area, "cm²")
elif num_lados == 4:
  area = medida_lado ** 2  # fórmula da área do quadrado
  print("QUADRADO, área:", area, "cm²")
elif num_lados == 5:
  print("PENTÁGONO")
  exit
else:
  print("POLÍGONO NÃO IDENTIFICADO")
  exit
