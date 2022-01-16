#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

from math import hypot

catop = float(input('Entre com o valor do cateto oposto: '))
catad = float(input('Entre com o valor do cateto adjacente: '))

print(' O valor do cateto oposto é :{} \n O valor do cateto adjacente é :{} \n O valor da hipoteusa é: {:.2f}'.format(catop,catad,hypot(catop,catad)))


#RESOLUÇÃO SEM IMPORTAÇÃO
catop = float(input('Entre com o valor do cateto oposto: '))
catad = float(input('Entre com o valor do cateto adjacente: '))
hip = (catop ** 2 + catad ** 2) ** (1/2)
print(' O valor do cateto oposto é :{} \n O valor do cateto adjacente é :{} \n O valor da hipoteusa é:{:.2F}'.format(catop,catad,hip))