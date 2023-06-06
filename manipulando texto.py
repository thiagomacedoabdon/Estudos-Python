frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[::2])
print(frase[13:])
print(frase[1:15:2])
print(frase[1:15:2])
print(frase[5::2])

# Para analise

print(frase.count('o')) #contar quantas vezes aparece a letra o
print(len(frase)) #número total de caracteres
print(frase.find('video')) #procurar quantas vezes tem video na frase
print(frase.find('Vídeo')) #procurar quantas vezes tem Video na frase


# Para transformação

print(frase.replace('Python', 'JS')) #'coloco a palavra que quero trocar', 'coloco a nova palavra'
print(frase.upper()) #coloca as letras que não estão ainda em maiusculo
print(frase.lower()) #coloca as letras que não estão ainda em minuscula
print(frase.capitalize()) #deixa apenas a primeira letra maiuscula
print (frase.title()) #cada inicio das palavras ficam em maiusculo
print(frase.strip()) #remove todos os espaços inuteis no inicio e no fim
print(frase.rstrip()) #remove todos os espaços inuteis no fim
print(frase.lstrip()) #remove todos os espaços inuteis do início
print(len(frase.strip())) #apos remover os espaços em branco, conta os caracteres

# Para divisão

print(frase.split()) #cria uma divisão nas palavras com indexação nova com novas listas/numerações

# Para unir

print('-'.join(frase)) #junta a frase com o separador. Pode ser qualquer outra coisa





