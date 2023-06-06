s = float(input('Qual o valor do salário do funcionário? R$'))
ns = s + (s * 15 / 100)
print ('O salário do funcionário é R${:.2f}, com o aumento de 15%, passará para {:.2f}'.format(s, ns))
