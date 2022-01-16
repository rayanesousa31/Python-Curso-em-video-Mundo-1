#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

func = str(input('Qual o seu nome? '))

sal = float(input('Qual o valor do seu salário? R$'))

new = sal + (sal * (15.0/100))

print('Seu salário com reajuste é R$ {:.2f}'.format(new))