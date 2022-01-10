# Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print('Aparece', frase.upper().count('A'),'vezes')
print('A 1ª vez, na posição', frase.find('A') + 1)
print('A última vez, na posição', frase.rfind('A') + 1)