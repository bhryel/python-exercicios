# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipoternusa.

from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)

print('O valor da hipotenusa é {:.2f}'.format(hi))
