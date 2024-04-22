Lparede = float(input('Largura da parede: '))
Aparede = float(input('Altura da parede: '))
area = float(Lparede * Aparede)
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'
      .format(Lparede, Aparede, area))

print('Para pintar essa parede, você precisa de {}L de tinta'
      .format(tinta))

