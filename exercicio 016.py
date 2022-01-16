#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
#ex: digite um número 6.217. O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um valor: '))

print('O número {} tem a parte inteira {}'.format(num,(trunc(num))))


#outra forma sem importar math

num = float(input('Digite um valor: '))

print('O número {} tem a parte inteira {}'.format(num,(int(num))))