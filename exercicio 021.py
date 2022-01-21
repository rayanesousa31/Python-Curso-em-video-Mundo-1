#Faça um programa em python que abra e reproduza o audio de arquivo MP3.
#tocando arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load("gaga.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
input()
