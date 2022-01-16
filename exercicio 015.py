#Escreva um programa que pergunte quantos quilômetros foram percorridos por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado. Calcle o valor do preço
#a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por quilometro rodado.

km = float(input('Quantos quilômetros (km) foram percorridos?'))
dias  = int(input('Quantidade de dias do aluguel do carrro: '))

print('O valor a ser pago é de R$ {:.2f}'.format((km*0.15)+(dias*60.00)))