# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


from math import trunc

numero = float(input('Digite um número real: '))

print('A parte inteiro do número {} é {}'.format(numero, trunc(numero)))