import pygame

def rot_center(image, rect, angle):  # Rotate image around center, common pygame code
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def draw_ships(win, blueShip, redShip):
    blue_image, blue_rect = rot_center(
        blueShip.surface, blueShip.pos, blueShip.rotation)
    win.blit(blue_image, blue_rect)

    red_image, red_rect = rot_center(
        redShip.surface, redShip.pos, redShip.rotation)
    win.blit(red_image, red_rect)
