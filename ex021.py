# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

input('Tecle algo para encerrar: ')
