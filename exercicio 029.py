#Escreva um programa que leia a velocidade de um carro.
#Se ela ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite

vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    
    print('Você acaba de ser multado. O valor da sua multa será :R$ {}. '.format((vel-80)*7.00))

else:
    print('Tanha uma boa viagem!')