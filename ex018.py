# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {}ª, o SENO é {:.2f}'.format(angulo, seno))
print('O ângulo de {}ª, o COSSENO é {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}ª, a TANGENTE é {:.2f}'.format(angulo, tangente))
