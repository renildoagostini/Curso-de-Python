#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Informe o valor do produto: '))
desconto = produto - (produto * 5)/100

print('O produto com desconto de 5% equivale a: R$ {:.2f}'.format(desconto))