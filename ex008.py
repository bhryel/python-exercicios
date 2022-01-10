# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

m = float(input('Digite quanto metros: '))
print('A medida de {}m, corresponde a {}cm e {}mm'.format(m, m*100, m*1000))
print('{}m equivale a {}km (kilômetros)'.format(m, m/1000))
print('{}m equivale a {}hm (hectômetro)'.format(m, m/100))
print('{}m equivale a {}dam (decâmetro)'.format(m, m/10))
print('{}m equivale a {}dm (decímetro)'.format(m, m*10))
