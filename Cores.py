'''
para style:
0 - Não altera nada
1 - negrito
4 - sublinado
7 - inverte as cores

para cor do text:
29 branco
30 preto
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo
36 azul claro
37 cinza

para o backgroud:
40 fundo branco
41 fundo vermelho
42 fundo verde
43 fundo amarelo
44 fundo azul
45 fundo roxo
46 fundo azul claro
47 fundo cinza
'''

print('\033[0;29;44mOlá, mundo!\033[m')
nome = 'Thiago'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))
