# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.


quant_macas = int(input("Digite a quantidade de maçãs compradas: "))


if quant_macas < 12:
    preco_unidade = 0.3
else: preco_unidade = 0.25
valor_compra = quant_macas * preco_unidade
print(f"O valor total da compra é de R$ {valor_compra:.2f}")




 
