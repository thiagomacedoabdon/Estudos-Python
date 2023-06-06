print('='*30)
print('Analisador de triângulos')
print('='*30)

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro seguimento:'))

if r1<r2+r3 and r2<r1+r3 and r3<r2+r1:
    print('Os seguimentos podem formar um triângulo!')
else:
    print('Os seguintes não formam um triângulo!')
