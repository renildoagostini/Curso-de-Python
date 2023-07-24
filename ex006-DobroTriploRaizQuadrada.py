# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quaadrada

from math import sqrt

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = sqrt(numero)

print('Dobro: {}'.format(dobro))
print('Triplo: {}'. format(triplo))
print('Raiz quadrada {:.2}' . format(raizQuadrada))