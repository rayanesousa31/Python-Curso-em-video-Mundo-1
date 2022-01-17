#Crie um programa inteiro e mostre na tela se ele é par ou impar.

num = int(input('Digite um númer inteiro:'))

resultado = (num%2)

if  resultado == 1 :
    print('O numero {} é impar.'.format(num))

else:
    print ('O numero {} é par'.format(num))