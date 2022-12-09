import pygame
import math
import time

from menu import *
from bullets import *
from drawShip import *
from shipManagement import *
from gameOver import *

# Arcade controlls:
# main (Left player)
# direction: arrow-keys

# buttons:
# lshift space z
# lalt/opt lctrl c

# sec (Right player)
# direction: drgf (left, up, right, down)

# buttons:
# qwi
# sao

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Draws game in fullscreen
WIDTH, HEIGHT = pygame.display.get_surface().get_size() # Gets and saves screen size
pygame.display.set_caption("Agroids") # Sets window caption to Agroids
FPS = 30 # Sets framerate to 30 FPS

# Decides which path to use: (Arcade uses piPath, computer uses compPath)
piPath = "/home/pi/RetroPie/roms/pc/assets/"
compPath = "./assets/"
path = compPath

# Classes for the ships:
class blueShip:
    shipSurface = pygame.image.load(path + "blueShip.png").convert_alpha()
    shipSurface = pygame.transform.scale(shipSurface, (56, 52))

    surface = shipSurface
    pos = pygame.Rect(WIDTH/4-54, HEIGHT/2, 70, 70)
    rotation = 0
    spawnPos = [WIDTH/4-54, HEIGHT/2]
    exactPos = spawnPos
    bullets = []
    shotTime = 0
    hp = 3


class redShip:
    shipSurface = pygame.image.load(path + "redShip.png").convert_alpha()
    shipSurface = pygame.transform.scale(shipSurface, (56, 52))

    surface = shipSurface
    pos = pygame.Rect(WIDTH/4*3, HEIGHT/2, 70, 70)
    rotation = 0
    spawnPos = [WIDTH/4*3, HEIGHT/2]
    exactPos = spawnPos
    bullets = []
    shotTime = 0
    hp = 3


# Initialize sprites:
space = pygame.image.load(path + "space.png").convert_alpha()
space = pygame.transform.scale(space, (WIDTH, HEIGHT))

heartFull = pygame.image.load(path + "heartFull.png").convert_alpha()
heartFull = pygame.transform.scale(heartFull, (48, 40))

heartEmpty = pygame.image.load(path + "heartEmpty.png").convert_alpha()
heartEmpty = pygame.transform.scale(heartEmpty, (48, 40))

# Set some good variables:
gameMode = "menu"
winner = None
started = False
gameStartDelay = 0

def draw_hearts(): # Draws the players hp to the screen
    for i in range(1,4): # i will have values from 1 to 3
        if i <= blueShip.hp:
            win.blit(heartFull, (20+60*(i-1), 20))
        else:
            win.blit(heartEmpty, (20+60*(i-1), 20))
    
    for i in range(1,4): # i will have values from 1 to 3
        if i <= redShip.hp:
            win.blit(heartFull, (WIDTH-20-48-60*(3-i), 20))
        else:
            win.blit(heartEmpty, (WIDTH-20-48-60*(3-i), 20))

def draw_window(): # Function called from main() to draw things
    win.blit(space, (0, 0)) # Draws the background

    if gameMode == "menu":
        draw_menu(win)

    elif gameMode == "pVSp" and not started:
        draw_ships(win, blueShip, redShip)
        draw_hearts()

    elif gameMode == "pVSp":
        draw_ships(win, blueShip, redShip)
        draw_bullets(win, blueShip, redShip)
        draw_hearts()

    elif gameMode == "gameOver":
        draw_game_over(winner, win, WIDTH, HEIGHT)
        draw_hearts()

    # If problematic use pygame.display.flip()!
    pygame.display.update()

def reset(): # Resets game state
        global started
        started = False
        blueShip.bullets = []
        redShip.bullets = []
        blueShip.exactPos = [WIDTH/4-54, HEIGHT/2]
        redShip.exactPos = [WIDTH/4*3, HEIGHT/2]
        blueShip.rotation = 0
        redShip.rotation = 0

def check_hp():
    global gameMode
    global winner
    global started
    if redShip.hp < 1:
        started = False
        gameMode = "gameOver"
        winner = "Blue"

    if blueShip.hp < 1:
        started = False
        gameMode = "gameOver"
        winner = "Red"

def check_bullet_overlapping(): # Checks if the bullets are intersecting anything
    for bullet in redShip.bullets:
        distance = [bullet[0] - blueShip.exactPos[0]-28,
                    bullet[1] - blueShip.exactPos[1]-26]
        if distance[0] < 25 and distance[0] > -25 and distance[1] < 25 and distance[1] > -25: # Hitbox is circular, radius 25
            blueShip.hp -= 1
            reset()

    for bullet in blueShip.bullets:
        distance = [bullet[0] - redShip.exactPos[0]-28,
                    bullet[1] - redShip.exactPos[1]-26]
        if distance[0] < 25 and distance[0] > -25 and distance[1] < 25 and distance[1] > -25: # Hitbox is circular, radius 25
            redShip.hp -= 1
            reset()


def shoot(key, ship): # Handles the shoot event
    if key:
        global shotTime # A wait time so you can't spray toooo fast
        if time.time() - ship.shotTime > 0.5:
            # Calculates bullet spawn position and sets rotation
            bullet = [ship.pos.x+36+26*math.cos((ship.rotation+90) * 3.1415 / 180),
                      ship.pos.y+34+24*math.sin((ship.rotation+270) * 3.1415 / 180), ship.rotation]
            ship.bullets.append(bullet) # Appends the bullet to the ships bullets list
            ship.shotTime = time.time() # Resets shotTime


def main(): # Main loop that calls all the functions
    global started # Handles if the game is actually started or not when ships and everything are rendered
    clock = pygame.time.Clock() # A clock for ticking frames
    run = True # Set false and the game loop ends
    while run: # Run game if run == True
        for event in pygame.event.get(): # Checks if someone closed the game window
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed() # Gets a list of all keys that are pressed

        # Exit the game with ESCAPE and on the Arcade closing the game is done by other buttons...
        if keys_pressed[pygame.K_ESCAPE] or keys_pressed[pygame.K_h] and keys_pressed[pygame.K_y] or keys_pressed[pygame.K_j] and keys_pressed[pygame.K_u]:
            run = False

        global gameMode # gameMode can be menu, pVSp and soon pVSai!! 
        if gameMode == "menu": # Renders the menu
            gameMode, gameStartDelay = update_menu(keys_pressed, gameMode)

        elif gameMode == "pVSp" and started: # Updates everything that're nessecary for the main game to run
            movement(keys_pressed, blueShip, "blue", HEIGHT, WIDTH)
            movement(keys_pressed, redShip, "red", HEIGHT, WIDTH)
            shoot(keys_pressed[pygame.K_LALT], blueShip)
            shoot(keys_pressed[pygame.K_s], redShip)

            move_bullets(blueShip, redShip, HEIGHT, WIDTH)
            check_bullet_overlapping()
            check_hp()

        elif gameMode == "pVSp" and not started: # Let's people rest a little before starting and between deaths
            # Resets ship positions, because I couldn't get it to work in any other way...
            blueShip.exactPos = [WIDTH/4-54, HEIGHT/2]
            redShip.exactPos = [WIDTH/4*3, HEIGHT/2]
            blueShip.pos.x = WIDTH/4-54
            blueShip.pos.y = HEIGHT/2
            redShip.pos.x = WIDTH/4*3
            redShip.pos.y = HEIGHT/2
            # Starts game if either shoot button is pressed down, also has some wait time so it doesn't get triggered when accepting in the menu
            if (keys_pressed[pygame.K_LALT] or keys_pressed[pygame.K_s]) and time.time() - gameStartDelay > 0.1:
                started = True

        draw_window() # Calls the draw function to actually display stuff
        clock.tick(FPS) # Makes the framerate correct

    pygame.quit() # Quits the game when run == False


if __name__ == "__main__": # Checks that this is the file actually executed from the terminal
    main()
