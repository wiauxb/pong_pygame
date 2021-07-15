import pygame
from pygame.locals import *
from constants import *
from player import Player
from ball import Ball
from score import Score
from sounds import *

pygame.init()

wnd = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Pong")

stop_main_loop = False

player1 = Player(wnd, MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
player2 = Player(wnd, WIDTH-PLAYER_WIDTH-MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
score = Score(wnd)
ball = Ball(wnd, WIDTH/2, HEIGTH/2, speed=0)

pressed_keys = {"p1_up": False, "p1_down": False, "p2_up": False, "p2_down": False}

def reset_game():
    global player1, player2, ball
    player1 = Player(wnd, MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
    player2 = Player(wnd, WIDTH-PLAYER_WIDTH-MARGE, (HEIGTH-PLAYER_HEIGTH)/2, PLAYER_WIDTH, PLAYER_HEIGTH)
    ball = Ball(wnd, WIDTH/2, HEIGTH/2)
    draw_game()
    point.play()
    pygame.time.delay(500)

def draw_game():
    pygame.draw.rect(wnd, "black", Rect(0, 0, WIDTH, HEIGTH))
    player1.draw()
    player2.draw()
    ball.draw()
    score.draw()
    pygame.display.flip()

def handle_events():
    global stop_main_loop, pressed_keys
    for event in pygame.event.get():
        if event.type == QUIT:
            stop_main_loop = True
        if event.type == KEYDOWN:
            if event.key == K_UP:
                pressed_keys["p2_up"] = True
            elif event.key == K_DOWN:
                pressed_keys["p2_down"] = True
            elif event.key == K_z:
                pressed_keys["p1_up"] = True
            elif event.key == K_s:
                pressed_keys["p1_down"] = True
            elif event.key == K_SPACE:
                reset_game()
            elif event.key == K_ESCAPE:
                stop_main_loop = True
        if event.type == KEYUP:
            if event.key == K_UP:
                pressed_keys["p2_up"] = False
            elif event.key == K_DOWN:
                pressed_keys["p2_down"] = False
            elif event.key == K_z:
                pressed_keys["p1_up"] = False
            elif event.key == K_s:
                pressed_keys["p1_down"] = False

    if pressed_keys["p2_up"]:
        player2.move(-PLAYER_SPEED)
    if pressed_keys["p2_down"]:
        player2.move(PLAYER_SPEED)
    if pressed_keys["p1_up"]:
        player1.move(-PLAYER_SPEED)
    if pressed_keys["p1_down"]:
        player1.move(PLAYER_SPEED)

clock = pygame.time.Clock()

while not stop_main_loop:
    clock.tick(TIME_RATE)
    handle_events()
    ball.step(player1.rect, player2.rect, reset_game, score)
    draw_game()
    
pygame.quit()