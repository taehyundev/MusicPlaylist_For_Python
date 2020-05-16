import pygame
file = '오반 (OVAN) - 행복 Happiness [Music Video].mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.