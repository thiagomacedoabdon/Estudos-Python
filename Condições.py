'''#Exemplo teoria
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('-- FIM --')

#condição simplificada

tempo = int(input('Quantos anos tem seu carro?'))
print ('Carro novo' if tempo <=3 else 'Carro velho')
print('-- FIM --')
'''
#aula pratica
nome = str(input('Qual é seu nome?')).strip()
if nome == 'Thiago':
    print('Bom dia, {}! Que nome lindo você tem!'.format(nome))
else:
    print('Poxa, {}!!! Seu nome poderia ser melhor!'.format(nome))

#outro exemplo
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = ((n1+n2+n3)/3)
print('A sua média foi {:.1f}'.format(m))
if m <=6.0:
    print('Sua média não foi o bastante. Você está reprovado!')
if m>=6.0 and m<=8.0:
    print('Sua média foi boa. Você está aprovado!')
else:
    print('Sua média foi ótima. Você foi aprovado!')
    