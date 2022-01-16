#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Nome do aluno(a) : ')

nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))
med = (nota1 + nota2)/2
print(' A média final do(a) aluno(a) {} é {:.1f}.'.format(nome,med)) 