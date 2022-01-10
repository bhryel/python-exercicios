# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o salário do funcionário? R$'))
if salario >= 1250:
    salAtual = salario + (salario * 0.10)
    print('Seu salário de ${:.2f}, teve um reajuste de 10%, agora será de ${:.2f}.'.format(salario, salAtual))
else:
    salAtual = salario + (salario * 15 / 100)
    print('Seu salário de ${:.2f}, teve um reajuste de 15%, agora será de ${:.2f}'.format(salario, salAtual))
