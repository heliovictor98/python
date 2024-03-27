print('='*40)
dia = int(input('Quantos dias ficou alugado? '))
km = float(input('Quantos KM foram rodados? '))

valorCarroDia = 60
valorKmRodado = 0.15

valorTotalDia = dia * valorCarroDia
valorTotalKm = km * valorKmRodado

print('='*40)
print('Valor total Km = R${}'
      '\nValor total Diaria = R${}'
      '\nO Custo total do carro e de = R${}'
      .format(valorTotalKm, valorTotalDia,valorTotalDia+valorTotalKm))
print('='*40)