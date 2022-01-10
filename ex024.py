# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Qua o nome da cidade? ')

print('SANTO' in cidade.upper().split()[0])