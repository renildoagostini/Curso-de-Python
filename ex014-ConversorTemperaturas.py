# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input('Informe a quantidade de dias que o veículo ficou alugado: '))
km = float(input('Informe o total de kilometros rodados: '))

valorDia = dias * 60.00
valorKm = km * 0.15
valorFinal = valorDia + valorKm

print('O valor total a pagar é de R$ {:.2f}'.format(valorFinal))