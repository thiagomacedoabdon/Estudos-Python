n = int(input('Que ano quer analisar? '))
if n % 4 == 0 and n % 100 != 0 or n % 400 ==0:
    print( 'O ano {} é bissexto!'.format(n))
else:
    print('O ano {] não é bissexto!'.format(n))
