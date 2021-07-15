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
        self.hitbox = pygame.draw.circle(self.surface, "white", (self.x, self.y), self.size/2)

    def draw(self):
        self.hitbox = pygame.draw.circle(self.surface, "white", (self.x, self.y), self.size/2)

    def check_player_collision(self, player1, player2):
        if self.hitbox.colliderect(player1):
            overlapping = self.hitbox.clip(player1)
            if overlapping.width > overlapping.height:
                self.direction *= -1
            else:
                self.direction = math.pi - self.direction
            return True
        elif self.hitbox.colliderect(player2):
            overlapping = self.hitbox.clip(player2)
            if overlapping.width > overlapping.height:
                self.direction *= -1
            else:
                self.direction = math.pi - self.direction
            return True
        return False

    def check_window_collision(self, reset_game, score):
        rep = False
        bounds = self.surface.get_rect()
        if self.x - self.size/2 < bounds.left:
            score.P2 += 1
            reset_game()
            rep = True
        elif self.x + self.size/2 > bounds.right:
            score.P1 += 1
            reset_game()
            rep = True
        if self.y - self.size/2 < bounds.top or self.y + self.size/2 > bounds.bottom:
            self.direction *= -1
            rep = True
        return rep

    def check_collisions(self, player1, player2, reset_game, score):
        if self.check_player_collision(player1, player2):
            collision.play()
            return
        if self.check_window_collision(reset_game, score):
            collision.play()

    def step(self, player1, player2, reset_game, score):
        self.check_collisions(player1, player2, reset_game, score)
        self.x += self.speed*math.cos(self.direction)
        self.y += self.speed*math.sin(self.direction)