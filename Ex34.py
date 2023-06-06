n = float(input('Qual o salário do funcionário? '))
if n >= 1250.00:
    n = (n*10)/100+n
    print('O salário reajustado do funcionário será R${}'.format(n))
else:
    n = (n*15)/100+n
    print('O salário reajustado do funcionário será R${}'.format(n))
