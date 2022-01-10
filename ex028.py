# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

maq = randint(0, 5) # Faz o computador "pensar"
linha = '-=-' * 20
print(linha)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(linha)
num = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print ('PROCESSANDO...')
sleep(3)
if num == maq:
    print('Parabéns, você VENCEU! eu pensei em {}'.format(maq))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(maq, num))
