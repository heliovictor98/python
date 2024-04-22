import math
import emoji

print('='*40)
print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))
num = int(input('Digite um número'))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

print('='*40)