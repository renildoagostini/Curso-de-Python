# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))

print('Seno de {} é: {:.2f}' . format(angulo, sin(radians(angulo))))
print('Cosseno de {} é {:.2f}' .format(angulo, cos(radians(angulo))))
print('Tangente de {} é {:.2f}' .format(angulo, tan(radians(angulo))))


