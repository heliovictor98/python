compraConfirmada = True
dadosCompra = 'Compra no valor de R$12.50 e entraga confirmada'

for enviar in range(3):
    if compraConfirmada:
        print(dadosCompra)
        print('Detalhes enviado para o seu email')
        break
else:
    print('Falha na compra')
