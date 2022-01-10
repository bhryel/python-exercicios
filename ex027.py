# Faça um programa o nome completo de uma passoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Souza: Souza

nome = input('Qual seu nome completo? ')
print('Primeiro:', nome.split()[0])
print('Último:', nome.split()[-1])
