from random import randint
from time import sleep
computador = randint(0, 10)

print('=' * 60)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('=' * 60)

jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Parabéns! Você conseguiu vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))
