#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#Resolução Rayane:
temp = float(input('Digite a temperatura em Celsius: '))

F = (temp * 1.8) + 32
K = temp + 273.15

print('A temperatura convertida de Celsius para Fahrenheit é {:.2f} \n A tempertaura convertida de Celsius para Kelvin é {:.2f}'.format(F,K))


#Resolução Granabara
temp = float(input('Informe a temperatura em Celsius'))

F = ((9*temp)/5) + 32
