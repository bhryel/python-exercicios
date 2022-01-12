# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

opcao = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^40}'.format(' JOKENPÔ '))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador < 0 or jogador > 2: # validação de opção inválida
    print('\033[1;31mJOGADA INVÁLIDA, TENTE NOVAMENTE!\033[m')
else:
    #contagem dinâmica
    print('JO..', end='')
    sleep(1)
    print('KEN..', end='')
    sleep(1)
    print('PÔ!!!')

    #resultados
    print('-=' * 12)
    print('Computador jogou {}'.format(opcao[computador]))
    print('Jogador jogou {}'.format(opcao[jogador]))
    print('-=' * 12)

    if computador == 0: # computador escolhe Pedra
        if jogador == 0:
            print('\033[1;33mEMPATE!\033[m')
        elif jogador == 1:
            print('\033[1;32mJOGADOR VENCE!\033[m')
        elif jogador == 2:
            print('\033[1;32mCOMPUTADOR VENCE!\033[m')
        else:
            print('\033[1;31mJOGADA INVÁLIDA!\033[m')
    elif computador == 1: # computador escolhe Papel
        if jogador == 0:
            print('\033[1;32mCOMPUTADOR VENCE!\033[m')
        elif jogador == 1:
            print('\033[1;33mEMPATE!\033[m')
        elif jogador == 2:
            print('\033[1;32mJOGADOR VENCE!\033[m')
        else:
            print('\033[1;31mJOGADA INVÁLIDA!\033[m')
    elif computador == 2: # computador escolhe Tesoura
        if jogador == 0:
            print('\033[1;32mJOGADOR VENCE!\033[m')
        elif jogador == 1:
            print('\033[1;32mCOMPUTADOR VENCE!\033[m')
        elif jogador == 2:
            print('\033[1;33mEMPATE!\033[m')
        else:
            print('\033[1;31mJOGADA INVÁLIDA!\033[m')
