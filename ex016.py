#Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite 6.127 e mostre 6 somente.
from math import trunc

n = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(n, trunc(n)))
