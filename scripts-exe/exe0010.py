valor = float(input('Quanto dinheiro você tem? R$'))
dolar = float(3.27)

print('Com R${} você pode comprar U${:.2f}'.format(valor, valor/dolar))
