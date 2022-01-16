#Faça um programa que leia um ângulo qualquer e mostrena tela o valor do seno, cosseno e tangente.

from math import radians ,sin, cos, tan
ang = float(input('Qual o valor do angulo que gostaria de ter as informações?'))

print('O angulo {} tem o seno no valor de {:.2f} \n Cossseno no valor de {:.2f} \n E tangente no valor de {:.2f}'.format(ang,sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))