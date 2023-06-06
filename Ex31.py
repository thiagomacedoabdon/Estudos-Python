from time import sleep

n = int(input('Qual a distância da viagem em KM? '))
print ('Processando...')
sleep(0.5)

if n <= 200:
    n1 = n*0.50
    print('O valor a pagar para {}km, é um total de R${:.2f}'.format(n, n1))
else:
    n2 = n*0.45
    print('O valor a pagar para {}km, é um total de R${:.2f}'.format(n, n2))
