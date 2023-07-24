# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.


from math import hypot


catetoOposto = float(input('Informe o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Informe o comprimento do cateto adjacente: '))

#co = pow(catetoOposto,2)
#ca = pow(catetoAdjacente,2)

#hipotenusa = ca + co

#h = math.sqrt(hipotenusa)

h = hypot(catetoOposto,catetoAdjacente)

print('Hipotenusa é: {:.2f}'. format(h))