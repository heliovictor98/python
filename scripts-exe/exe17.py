co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('O valor e {:.2f}'.format(hi))