# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

altura = float(input('Qual é sua altura? (m) '))
peso = float(input('Qual é seu peso? (Kg) '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está \033[1;33mabaixo do peso\033[m normal!')
elif imc <= 25:
    print('Parabéns! Você está na faixa de \033[1;32mPESO NORMAL\033[m')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Você está em \033[1;31mObesidade!\033[m')
else:
    print('Você está em \033[1;31mObesidade mórbida\033[m, cuidado!')
