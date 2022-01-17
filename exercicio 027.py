#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
#o primeiro e o último nome separadamente

nome = str(input('Digite o seu nome completo:'))
nc = nome.split()
print(nc)
print('Seu primeiro nome é {}'.format(nc[0]))
print('Seu sobrenome é {}'.format(nc[len(nc)-1]))