 #Crie um programa que leia o nome completo de uma pessoa e mostre:
 #-O nome con todas as letras maiúsculas
 #-O nome com todas as letras minúsculas
 #-Quantas eltras ao todo (sem considerar espaços)
 #-Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() 

print('Seu nome em maiúscula é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))
