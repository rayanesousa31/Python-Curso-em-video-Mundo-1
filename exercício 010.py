#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos 
#dólares ela pode comprar - Considere USS 1,00 = R$ 3,27

din = float(input('Quanto dinheiro você tem em real? R$'))

print('Você consegue comprar USS {:.2f} dólares'.format(din/3.27))