import math
n = float(input('Digite um número real qualquer:'))
print ('O número {} tem a parte inteira {}'.format(n, math.trunc(n)))

# OU PODE SER ASSIM TAMBÉM

from math import trunc
n = float(input('Digite um número real qualquer:'))
print ('O número {} tem a parte inteira {}'.format(n, trunc(n)))

# OU PODE SER ASSIM TAMBÉM

n = float(input('Digite um número real qualquer:'))
print ('O número {} tem a parte inteira {}'.format(n, int(n)))
