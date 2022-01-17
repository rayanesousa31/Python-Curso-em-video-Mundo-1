#Desenvolva um programa que pergunte a distância de uma viagem em km. 
#Calcule o preço da passagem, cobrando R$0,50 por km rodado para viagens 
#de até 200km e R$0,45 para viagens mais longas.

dist = float(input('Qual a distancia em km a percorrer? '))

d1 = dist * 0.50

if dist <= 200:
    print('O valor da passagem será R$ {}'.format(d1))

else:
    print('O valor da passagem será R${}'.format(dist*0.45))    

    