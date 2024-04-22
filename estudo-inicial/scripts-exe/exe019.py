import random
aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Primeiro Aluno: '))
aluno3 = str(input('Primeiro Aluno: '))
aluno4 = str(input('Primeiro Aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)
print('Aluno escolhido foi: {}'.format(escolhido))

