#Escreva um programa que pergunte o salário de um funcionário e 
#calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
#Para os inferiores ou iguais é de 15%.

nome = str(input('Olá! Qual o seu nome? '))
sal = float(input('Por favor, digite o valor do seu salário: '))

if sal > 1250.00:
    print('Seu salário teve um aumento de 10%. \nSeu salário atualizado é  {:.2f}'.format((sal + (sal * 10/100))))

else:
    print('Seu salário teve um aumento de 15%.\nSeu salário atualizado é {:.2f}'.format ((sal + (sal * 15/100))))
