import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {:.1f}'.format (num, raiz))

# OU PODE SER ASSIM TAMBÉM

print ('-' * 12)

from math import sqrt
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {:.1f}'.format (num, raiz))

print ('-' * 12)

import random
num = random.random() #número inteiro de 0 a 1
print (num)

# OU PODE SER ASSIM TAMBÉM

import random
num = random.randint (1, 50) #número entre 1 e 50
print (num)

