# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

casa = float(input('Valor da casa? R$'))
salario = float(input('Salario do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
mensalidade = casa / (tempo*12)
print('ANALISANDO...')
sleep(3)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, tempo, mensalidade))
if mensalidade <= salario * 30 / 100:
    print('\033[1;32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo Negado!\033[m')
