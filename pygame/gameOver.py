import pygame
import time

pygame.font.init()
font = pygame.font.Font("./OpenSans-Bold.ttf", 65)

waitTime = 0

def set_waitTime(number):
    global waitTime
    waitTime = number

def draw_game_over(winner, win, WIDTH, HEIGHT):
    text = font.render(
        "GAME OVER!", True, (200, 10, 10))
    winnerText = font.render("Winner: " + winner, True, (10, 10, 10))
    win.blit(text, (WIDTH/2-170, HEIGHT/2-80))
    win.blit(winnerText, (WIDTH/2-170, HEIGHT/2-15))

def go_back(keys_pressed):
    if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_LALT]) and time.time() - waitTime > 2:
        return "resetAll"

    return None