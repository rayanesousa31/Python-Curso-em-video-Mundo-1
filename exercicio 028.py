#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
from random import randint

escolhido = randint (0 , 5)
print('Vamos brincar um pouco...'),time.sleep(3)
print('Vamos jogar um jogo de adivinhação...Em qual número estou pensando?'),time.sleep(3)
usuario = int(input('Qual número de 0 a 5 você escolhe? ')),time.sleep(3)
print('PROCESSSSANDO O RESULTADO...'),time.sleep(3)
if usuario == escolhido:
    print('Acertou!')

else:
    print('Errado')    




