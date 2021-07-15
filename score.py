import pygame
from constants import *


class Score:

    def __init__(self, surface):
        self.P1 = 0
        self.P2 = 0
        self.surface = surface
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)

    def draw(self):
        text= self.font.render(f'{self.P1} - {self.P2}', False, (255, 255, 255))
        self.surface.blit(text,((WIDTH-text.get_rect().width)/2,MARGE))

