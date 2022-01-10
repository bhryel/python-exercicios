# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('-=-' * 10)
print('    ALISTAMENTO MILITAR')
print('-=-' * 10)
print('''Qual seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Opção: '))
if sexo == 2:
    print('O Alistamento Militar é destinado somente ao público masculino.')
else:
    nascimento = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18-idade))
        print('Seu alistamento será em {}.'.format(nascimento+18))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
        print('Seu alistamento foi em {}.'.format(nascimento+18))
    else:
        print('Você tem que se alistar IMEDIAMENTE!')
