# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.#
# – Quantas letras ao todo (sem considerar espaços).#
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip() # strip() corta os espaços antes e depois dos caracteres

print('ANALIZANDO SEU  NOME')

print('Seu nome em maiúscula é {}' .format(nome.upper()))
print('Seu nome em minúacula é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras'. format(len(nome)-nome.count(' '))) #elimina os espaço entre as string
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))