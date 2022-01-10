# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maipusculas
# -> O nome com todas minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

nome = str(input('Qual seu nome? ')).strip()

print('Maiúsculas:', nome.upper())
print('Minúsculas:', nome.lower())
print('Qtd letras:', len(nome) - nome.count(' '))
print('Qtd letras 1º nome:', nome.find(' '))