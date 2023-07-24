# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

nome = input('Informe o nome do aluno: ')
nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

print('A média das notas do aluno {} foi: {:.2}' .format(nome, media))