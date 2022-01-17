#Faça um programa que leia um número de 0 a 9999 e mostre na 
#tela cada um dos digitos separados.
#ex:Digite um número
#unidade:4 | dezena:3 | centena:8 | milhar:1


#----podendo fazer dessa forma, porém no momento não é a melhor maneira-----
#num = int(input('Analisando o número '))
#num = str(num)
#print('Sua unidade é {}'.format(num[3]))
#print('Sua dezena é {}'.format(num[2]))
#print('Sua centena é {}'.format(num[1]))
#print('Seu milhar é {}'.format(num[0]))


num = int(input("Digite o número:"))
u = num // 1 % 10  # faz a divissão inteira do num por 1 e resto da divisão por 10.
print('A unidade é {}'.format(u))
d  = num // 10 % 10
print('A dezena é {}'.format(d))
c  = num // 100 % 10
print('A centena é {}'.format(c))
m  = num // 1000 % 10
print('A milhar é {}'.format(m))