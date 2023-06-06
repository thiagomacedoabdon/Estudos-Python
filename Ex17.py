co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
hi = (co**2 + ca**2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hi))

#ou pode ser assim também

import math
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
hi = math.hypot(co, ca)
print ('A hipotenusa vai medir {:.2f}'.format(hi))

#ou pode ser assim também

from math import hypot
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
hi = hypot(co, ca)
print ('A hipotenusa vai medir {:.2f}'.format(hi))