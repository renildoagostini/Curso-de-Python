# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 part viagens mais longas.

distacia = float(input('Informe a distacia percorrida da viagem: '))

print('Você está prestes a começar uma viagem de {}KM.'.format(distacia))

if distacia <= 200:
    print('E o preço de sua passagem será de R${:.2f}'.format(distacia * 0.50))
else:
    print('E o preço de sua passagem será de R${:.2f}'.format(distacia * 0.45))


