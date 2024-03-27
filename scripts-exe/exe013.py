salarioF = float(input('Qual é o salário? R$'))
vAumento = float(input('Quantos % de aumento? '))
vImposto = float(input('Quantos % de imposto '))

newSalario = salarioF + (salarioF*vAumento/100)
valorAumento =  (salarioF*vAumento/100)

valorImposto = (newSalario*vImposto/100)
valorLiquido = newSalario - (newSalario*vImposto/100)

print('O salario que era de R${}'
      '\nCom {}% de aumento, passou a ser de R${}'
      '\nFoi um aumento de R${}'
      '\nO Imposto de {} seria de R${}'
      '\nO valor liquido seria de R${}'
      .format(salarioF, vAumento, newSalario, valorAumento,vImposto, valorImposto,valorLiquido))
