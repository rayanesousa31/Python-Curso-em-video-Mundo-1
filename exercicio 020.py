#O mesmo professor do desafio anterior quer sortear a ordem de apresentação 
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
#mostre a ordem sorteados.

from random import shuffle  #shuffle = embaralhar em ingles

n1 = str(input('Nome do primeiro aluno : '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno : '))

lista = [n1,n2,n3,n4]

ordem = shuffle(lista)

print('A ordem de apresentação será:')
print(lista)