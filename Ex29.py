from time import sleep

v = float(input('Qual a velocidade do carro? '))
print('PROCESSANDO...')
sleep(0.5)

if v>80:
    print('Você ultrapassou o limite de velocidade.')
    print('A multa vai custar R${:.2f}'.format((v-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança!')
