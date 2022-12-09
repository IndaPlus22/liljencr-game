import pygame
import math

bulletSpeed = 12
bulletColor = (255, 255, 0)


def draw_bullets(win, redShip, blueShip):
    for bullet in redShip.bullets:
        rect = pygame.Rect(bullet[0]-4, bullet[1]-4, 8, 8) # Minus 4 cause position is saved as topleft
        pygame.draw.rect(win, bulletColor, rect)

    for bullet in blueShip.bullets:
        rect = pygame.Rect(bullet[0]-4, bullet[1]-4, 8, 8) # Minus 4 cause position is saved as topleft
        pygame.draw.rect(win, bulletColor, rect)


def move_bullets(blueShip, redShip, WIDTH, HEIGHT):
    for bullet in redShip.bullets:
        if bullet[0] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
            redShip.bullets.remove(bullet)
        bullet[0] -= bulletSpeed * math.cos((bullet[2]+270) * 3.1415 / 180)
        bullet[1] += bulletSpeed * math.sin((bullet[2]+270) * 3.1415 / 180)
    for bullet in blueShip.bullets:
        if bullet[0] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
            blueShip.bullets.remove(bullet)
        bullet[0] -= bulletSpeed * math.cos((bullet[2]+270) * 3.1415 / 180)
        bullet[1] += bulletSpeed * math.sin((bullet[2]+270) * 3.1415 / 180)
