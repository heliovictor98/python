valor1 = float(input('Quanto custa o produto: R$ '))
valor2 = valor1 -(valor1 *5/100)
final = valor1 - valor2

print('O valor do Produto é R${} \nE com o descoto de 5% ficou: R${} '
      '\nO valor do desconto foi de R${}'
      .format(valor1, valor2, final))