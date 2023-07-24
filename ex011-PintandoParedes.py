# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Informe a largura em metros da parede: '))
altura = float(input('Informe a altura em metros da parede: '))

area = altura * largura

cobertura = area / 2

print('Área: {} metros quadrados'. format(area))
print('Cobertura {}'. format(cobertura))