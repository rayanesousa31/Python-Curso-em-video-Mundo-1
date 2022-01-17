#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano para saber se é bisexto ou não, ou digite 0 para saber do ano atual: '))

if ano == 0:
    ano = date.today().year    #vai pegar o ano atual que esta na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  #ser divisivel por 4 e não divisivel por 100 portando diferente de zero
    print('o ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))