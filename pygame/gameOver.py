import pygame

pygame.font.init()
font = pygame.font.Font("./OpenSans-Bold.ttf", 65)


def draw_game_over(winner, win, WIDTH, HEIGHT):
    text = font.render(
        "GAME OVER!", True, (200, 10, 10))
    winnerText = font.render("Winner: " + winner, True, (10, 10, 10))
    win.blit(text, (WIDTH/2-170, HEIGHT/2-80))
    win.blit(winnerText, (WIDTH/2-170, HEIGHT/2-15))
