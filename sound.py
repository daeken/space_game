import pygame

pygame.mixer.init()

def play(name):
    pygame.mixer.music.load('sounds/' + name + '.wav')
    pygame.mixer.music.play()

# play('anthem apocalyptica')
