from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador "pensar"
print('-=- * 20')
print('Vou pensar em um número. Tente Adivinhar......')
print('-=- * 20')
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO....')
sleep(4)
if jogador == computador:
    print('Parabens, você ganhou')
else:
    print('Ganhei! eu pensei no número {} e não no número {}'.format(computador, jogador))


