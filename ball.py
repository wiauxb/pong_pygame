import random, math, pygame
from constants import *
from sounds import *

class Ball:

    def __init__(self, surface, x, y, size=BALL_SIZE, speed=BALL_DEFAULT_SPEED):
        self.surface = surface
        self.x = x
        self.y = y
        self.size = size
        self.direction = random.vonmisesvariate(0, 0)
        self.speed = speed
        self.old_pos = (x, y)
        self.hitbox = pygame.draw.circle(self.surface, "white", (self.x, self.y), self.size/2)

    def draw(self):
        self.hitbox = pygame.draw.circle(self.surface, "white", (self.x, self.y), self.size/2)

    
    def bounce(self, orientation):
        if orientation == "horizontal":
            self.direction *= -1
        elif orientation == "vertical":
            self.direction = math.pi - self.direction
        else:
            print("Not a valid bounce. Either horizontal or vertical")

    def save_pos(self):
        self.old_pos = (self.x, self.y)

    def step(self):
        self.save_pos()
        self.x += self.speed*math.cos(self.direction)
        self.y += self.speed*math.sin(self.direction)
        self.hitbox = pygame.draw.circle(self.surface, "white", (self.x, self.y), self.size/2)

    def move_back(self):
        self.x, self.y = self.old_pos