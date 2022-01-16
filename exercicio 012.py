#Façaum algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = float(input('O produto headset esta R$ '))

new = produto - (produto * (15.0/100))
new1 = produto - (produto * (10.0/100))

print('Pagando no pix você ganha 15% de desconto, ficando no valor de R$ {} \n no boleto 10% de desconto, ficando no valor de R${}'.format(new,new1))
