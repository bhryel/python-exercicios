# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b+c and b < a+c and c < a+b: # valida se é triângulo
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c: # valida se é equilátero
        print('EQUILÁTERO!')
    elif a != b != c != a: # valida se é escaleno
        print('ESCALENO!')
    else: # caso não for os anteriores é isósceles
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
