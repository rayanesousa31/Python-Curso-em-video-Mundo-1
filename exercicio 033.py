#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

a = int(input('Entre com o primeiro numero : '))
b = int(input('Entre com o segundo numero : '))
c = int(input('Entre com o terceiro numero : '))

if a < b and a < c:
    menor = a

if b < c and b < a:
    menor = b    

if c < b and c < a:
    menor = c

print('O menor valor é {}'.format(menor))    

if a > b and a > c:
    maior = a

if b > c and b > a:
    maior = b    

if c > b and c > a:
    maior = c

print('O maior valor é {}'.format(maior))    
