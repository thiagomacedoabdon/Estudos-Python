n = int(input('Escolha um número inteiro qualquer: '))
n1 = n%2
if n1 == 0:
    print('O {} é um número par!'.format(n))
else:
    print('O {} é um número ímpar!'.format(n))
