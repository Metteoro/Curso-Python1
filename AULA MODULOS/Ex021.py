import pygame
pygame.init()
pygame.mixer.music.load('be_someone.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()