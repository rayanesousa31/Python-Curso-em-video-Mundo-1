#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta
#necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m^2.

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual o altura da parede? '))
área = largura*altura

print('A parede com a dimensão {} e {} , temos a área no valor de : {}'.format(altura, largura ,(largura*altura)))

print('Será necessário {} litros de tinta para pintar a parede'.format(área/2))
