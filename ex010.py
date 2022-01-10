# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar
# Considere: US$1,00 = R$3,27

d = float(input('Quanto de dinheiro você tem na carteira? R$'))
print('Com R${:.2f}, você pode comprar {:.2f} de dólar americano'.format(d, d/5.51))
print('Com R${:.2f}, você pode comprar {:.2f} de dólar canadense'.format(d, d/4.43))
print('Com R${:.2f}, você pode comprar {:.2f} de euro'.format(d, d/6.39))
print('Com R${:.2f}, você pode comprar {:.2f} de iene'.format(d, d/0.049))
