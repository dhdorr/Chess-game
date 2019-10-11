import pygame
from pygame.sprite import Sprite

class Piece():
    def __init__(self, win):
        self.win = win

        self.image = pygame.image.load('images/pawn.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 37
        self.rect.centery = 37
        self.width = 45
        self.height = 45


    def update(self):
        self.rect = (self.rect.centerx, self.rect.centery, self.width, self.height)

    def blitme(self):
        self.win.blit(self.image, self.rect)