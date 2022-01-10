# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Digite o valor: '))
print('O valor com 5% de desconto fica R${:.2f}'.format(p-(p*(5/100))))
