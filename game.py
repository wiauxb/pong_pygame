import pygame
from constants import *
from player import Player
from score import Score
from ball import Ball
from sounds import *
from pygame.locals import *

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
            self.ball.step(self.player1.rect, self.player2.rect, self.reset_game, self.score)
            self.draw_game()