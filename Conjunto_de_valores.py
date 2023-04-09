import math

while True:
    valor = float(input("Digite um valor (digite um valor negativo ou zero para encerrar): "))
    if valor <= 0:
        break
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = math.sqrt(valor)
    print(f"Valor: {valor:.2f} | Quadrado: {quadrado:.2f} | Cubo: {cubo:.2f} | Raiz Quadrada: {raiz_quadrada:.2f}")

