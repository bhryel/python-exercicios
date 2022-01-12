# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJA '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual é a opção? '))
if pagamento == 1:
    total = preço - (preço * 10 / 100)
elif pagamento == 2:
    total = preço - (preço * 5 / 100)
elif pagamento == 3:
    total = preço
    parcela = total / 2
    print('SUa compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela, total / parcela))
else:
    total = preço
    print('Opção de pagamento \033[1;31mINVÁLIDA!\033[m Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
