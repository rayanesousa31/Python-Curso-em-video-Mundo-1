#Crie um programa que leia o nome de um cidade
# e diga se ela começa com o nome 'Santo'.

cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[0:5].upper() == 'SANTO')    #aparecer as 5 letras do santo e saber se a cidade digitada é igual a santo

