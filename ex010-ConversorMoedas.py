# crie um programa que leia um valor em real e converta para dolar. Cosidere U$1,00 = R$3,27

real = float(input('Informe o valor em real: '))
dolar = real / 4.92

print('O valor de R$ {} convertido em dolar é: US$ {:.3}'. format(real, dolar))