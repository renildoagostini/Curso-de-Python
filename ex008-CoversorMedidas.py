# escreva um programa que leia um valor em metros e o exiba convertido para centimetros e milimetros

metros = float(input('Digite a quantidade de metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('{} metros convertido em centimetros equivale a: {} Centimetros'. format(metros, centimetros))
print('{} metros convertidos em milimetros equivale a: {}  Milimetros' .format(metros, milimetros))