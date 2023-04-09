# Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1: feminino 2: masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:
# para homens: (72.7 * Altura) – 58
# para mulheres: (62.1 * Altura) – 44.7

import math

genero = int(input("Escolha o seu gênero: 1. Feminino, 2. Masculino ou 3. sair "))
altura = float(input("Digite a sua altura: "))
peso_ideal = float

if genero == 3:
    print("Saindo...")
    exit
if genero == 1:
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com altura de ", altura, "metros é: ", peso_ideal)
elif genero == 2:
    peso_ideal = (72.2 * altura) - 58
    print("O peso ideal para um homem com altura de: ", altura, "metros é: ", peso_ideal)
    


