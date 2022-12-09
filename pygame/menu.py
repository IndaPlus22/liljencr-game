from main import WIDTH, HEIGHT
import pygame
import time
pygame.font.init()

selected = 1

# Create a start button
playerVSplayer = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 - 80, 400, 80)
playerVSai = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 10, 400, 80)

font = pygame.font.Font("./OpenSans-Bold.ttf", 40)
playerVSplayerText = font.render("1 vs 1", True, (0, 0, 0))
playerVSaiText = font.render("1 vs AI", True, (0, 0, 0))

# Main game loop

buttonTime = 0


def update_menu(keys_pressed, gameMode):
    global selected
    global buttonTime
    if time.time() - buttonTime > 0.1:
        if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_f]):
            selected += 1
            buttonTime = time.time()
        elif (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_r]):
            selected -= 1
            buttonTime = time.time()

    if keys_pressed[pygame.K_LALT] or keys_pressed[pygame.K_s]:
        if selected == 1:
            gameMode = "pVSp"
        elif selected == 2:
            gameMode = "pVSai"

    if selected < 1:
        selected = 2
    elif selected > 2:
        selected = 1

    return gameMode, time.time()


def draw_menu(win):
    pVSpColor = (150, 150, 150)
    pVSaiColor = (150, 150, 150)
    if selected == 1:
        pVSpColor = (0, 200, 0)
    elif selected == 2:
        pVSaiColor = (0, 200, 0)

    pygame.draw.rect(win, pVSpColor, playerVSplayer)
    win.blit(playerVSplayerText, (playerVSplayer.x + 140, playerVSplayer.y + 10))

    pygame.draw.rect(win, pVSaiColor, playerVSai)
    win.blit(playerVSaiText, (playerVSai.x + 130, playerVSai.y + 10))
