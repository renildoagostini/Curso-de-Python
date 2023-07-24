# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Informe o primeiro seguimento: '))
b = int(input('Informe o segundo seguimento: '))
c = int(input('Informe o terceiro seguimento: '))

if a < b + c and b  < a + c and c < a + b:
    print('Os seguimentos acima podem formar triângulo')
else:
    print('Os seguimentos acima não podem formar triângulo')
