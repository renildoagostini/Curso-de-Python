#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o salario do funcionario: R$  '))

if salario > 1250:
    novoSalario = salario + (salario * 10) / 100
if salario <= 1250:
    novoSalario = salario + (salario * 15) / 100

print('O novo salario do funcionário será: R$ {:.2f}' .format(novoSalario))