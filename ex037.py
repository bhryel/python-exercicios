# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
      opcao = 'BINÁRIO'
      valor = bin(numero)
elif opcao == 2:
      opcao = 'OCTAL'
      valor = oct(numero)
elif opcao == 3:
      opcao = 'HEXADECIMAL'
      valor = hex(numero)
print('{} convertido para {} é igual a {}'.format(numero, opcao, valor[2:]))
#2: para eliminas a referencia do python 0b/0o/0h
