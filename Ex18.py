from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print('O ângulo {} tem o seno {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângilo {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo {} tem a tangete de {:.2f}'.format(angulo, tangente))
