import pygame
from pygame.locals import *
from constants import *

class Player:

    def __init__(self, surface, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface, "white", self.rect)

    def can_move(self, dy):
        bounds = self.surface.get_rect()
        if dy > 0:
            return self.rect.bottom + dy < bounds.bottom
        else:
            return self.rect.top + dy > bounds.top

    def move(self, dy):
        if self.can_move(dy):
            self.rect.move_ip(0,dy)
