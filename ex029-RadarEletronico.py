# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Informe a velocidade do veículo: '))
velFinal = vel - 80
valorPagar = velFinal * 7
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(valorPagar))
print('Tenha um bom dia! dirija com segurança')