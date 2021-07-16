import pygame
from constants import *
from player import Player
from score import Score
from ball import Ball
from sounds import *
from pygame.locals import *
import math

class Game:

    def __init__(self):
        self.wnd = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Pong")

        self.stop_main_loop = False

        self.player1 = Player(self.wnd, MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
        self.player2 = Player(self.wnd, WIDTH-PLAYER_WIDTH-MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
        self.score = Score(self.wnd)
        self.ball = Ball(self.wnd, WIDTH/2, HEIGTH/2, speed=0)

    def reset_game(self):
        self.player1 = Player(self.wnd, MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
        self.player2 = Player(self.wnd, WIDTH-PLAYER_WIDTH-MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
        self.ball = Ball(self.wnd, WIDTH/2, HEIGTH/2)
        self.draw_game()
        point.play()
        pygame.time.delay(500)

    
    def bounce_on_rect(self, rect):
        overlap = self.ball.hitbox.clip(rect)

        if overlap.width >= overlap.height:
            self.ball.bounce("horizontal")
        if overlap.width <= overlap.height:
            self.ball.bounce("vertical")


    def check_player_collision(self):
        if self.ball.hitbox.colliderect(self.player1.rect):
            self.bounce_on_rect(self.player1.rect)
            return True
        elif self.ball.hitbox.colliderect(self.player2.rect):
            self.bounce_on_rect(self.player2.rect)
            return True
        return False

    def check_window_collision(self):
        rep = False
        bounds = self.wnd.get_rect()
        if self.ball.x - self.ball.size/2 < bounds.left:
            self.score.P2 += 1
            self.reset_game()
            rep = True
        elif self.ball.x + self.ball.size/2 > bounds.right:
            self.score.P1 += 1
            self.reset_game()
            rep = True
        if self.ball.y - self.ball.size/2 < bounds.top or self.ball.y + self.ball.size/2 > bounds.bottom:
            self.ball.bounce("horizontal")
            rep = True
        return rep

    def check_collisions(self):
        if self.check_player_collision():
            collision.play()
            return True
        if self.check_window_collision():
            collision.play()
            return True
        return False

    def draw_game(self):
        pygame.draw.rect(self.wnd, "black", Rect(0, 0, WIDTH, HEIGTH))
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        self.score.draw()
        pygame.display.flip()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stop_main_loop = True

        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            self.reset_game()
        if keys[K_UP]:
            self.player2.move(-PLAYER_SPEED)
        if keys[K_DOWN]:
            self.player2.move(PLAYER_SPEED)
        if keys[K_z]:
            self.player1.move(-PLAYER_SPEED)
        if keys[K_s]:
            self.player1.move(PLAYER_SPEED)

    def run(self):
        clock = pygame.time.Clock()

        while not self.stop_main_loop:
            clock.tick(TIME_RATE)
            self.handle_inputs()
            self.ball.step()
            if self.check_collisions():
                self.ball.move_back()
            self.draw_game()