#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milimetros.

casa =  float(input('Quantos metros a casa mede? '))

cm = casa * 100
mm = casa * 1000

print('A metragem da casa em metros é {}m \nEm centímetros é {} cm \nEm milimetros é {} mm'.format(casa,cm, mm))