# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
if maior < num3:
    maior = num3
if menor > num3:
    menor = num3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))