import math
import pygame

speed = 7
rotChange = 6


def changeShipRot(increment, ship):
    ship.rotation += increment
    if ship.rotation > 359:
        ship.rotation -= 360
    elif ship.rotation < 0:
        ship.rotation += 360


def movement(keys_pressed, ship, color, WIDTH, HEIGHT):
    # Ships that go of screen will show up on the other side: (It has some offsets because of the pos being the top left corner of the ship)
    shipThruWall = 20 # How much of the ship needs to go thru the wall to activate
    wallOffset = 6
    if ship.exactPos[0] < 0-wallOffset-shipThruWall:
        ship.exactPos[0] = WIDTH-wallOffset-52+shipThruWall # 52 is ships height
    elif ship.exactPos[0] > WIDTH-wallOffset-52+shipThruWall:
        ship.exactPos[0] = 0-wallOffset-shipThruWall
    if ship.exactPos[1] < 0-wallOffset-shipThruWall:
        ship.exactPos[1] = HEIGHT-wallOffset-56+shipThruWall # 56 is ships width
    elif ship.exactPos[1] > HEIGHT-wallOffset-56+shipThruWall:
        ship.exactPos[1] = 0-wallOffset-shipThruWall

    # direction: drgf (left, up, right, down)
    red_keys = [pygame.K_r, pygame.K_f, pygame.K_d, pygame.K_g]
    blue_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    if color == "blue":
        keys = blue_keys
    else:
        keys = red_keys

    WSRot = 0
    if keys_pressed[keys[0]]:
        WSRot += 1
    if keys_pressed[keys[1]]:
        WSRot -= 1

    ADRot = 0
    if keys_pressed[keys[2]]:
        ADRot -= 1
    if keys_pressed[keys[3]]:
        ADRot += 1

    if WSRot != 0 and ADRot != 0:
        if WSRot == 1 and ADRot == 1:
            degreeGoal = 315
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation < degreeGoal and ship.rotation > degreeGoal-180:
                changeShipRot(rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(-rotChange, ship)

        elif WSRot == 1:
            degreeGoal = 45
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation > degreeGoal and ship.rotation <= degreeGoal+180:
                changeShipRot(-rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(rotChange, ship)

        elif ADRot == 1:
            degreeGoal = 225
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation < degreeGoal and ship.rotation > degreeGoal-180:
                changeShipRot(rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(-rotChange, ship)

        else:
            degreeGoal = 135
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation > degreeGoal and ship.rotation <= degreeGoal+180:
                changeShipRot(-rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(rotChange, ship)

    else:  # If not (W or S) AND (A or D) is pressed
        if WSRot == 1:
            degreeGoal = 0
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation > degreeGoal and ship.rotation <= degreeGoal+180:
                changeShipRot(-rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(rotChange, ship)
        elif WSRot == -1:
            degreeGoal = 180
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation < degreeGoal and ship.rotation > degreeGoal-180:
                changeShipRot(rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(-rotChange, ship)

        if ADRot == 1:
            degreeGoal = 270
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation < degreeGoal and ship.rotation > degreeGoal-180:
                changeShipRot(rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(-rotChange, ship)
        elif ADRot == -1:
            degreeGoal = 90
            if ship.rotation <= degreeGoal+rotChange and ship.rotation >= degreeGoal-rotChange:
                ship.rotation = degreeGoal
            if ship.rotation > degreeGoal and ship.rotation <= degreeGoal+180:
                changeShipRot(-rotChange, ship)
            elif ship.rotation != degreeGoal:
                changeShipRot(rotChange, ship)

    ship.exactPos[0] -= speed * math.cos((ship.rotation+270) * 3.1415 / 180)
    ship.exactPos[1] += speed * math.sin((ship.rotation+270) * 3.1415 / 180)
    ship.pos.x = int(ship.exactPos[0])
    ship.pos.y = int(ship.exactPos[1])
