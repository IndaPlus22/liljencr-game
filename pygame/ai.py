import pygame
import time
import math

# Holds meteors where meteor[0] is its rect and [1] is its moving direction and [2] is its rendered rotation and [3] is its exact position

speed = 7
rotChange = 6

def changeShipRot(increment, ship):
    ship.rotation += increment
    if ship.rotation > 359:
        ship.rotation -= 360
    elif ship.rotation < 0:
        ship.rotation += 360

def changeShipRotReturn(increment, degrees):
    rotation = degrees
    rotation += increment
    if rotation > 359:
        rotation -= 360
    elif rotation < 0:
        rotation += 360
    return rotation


def ai_script(blueShip, redShip, meteors, WIDTH, HEIGHT):
    # Ships that go of screen will show up on the other side: (It has some offsets because of the pos being the top left corner of the ship)
    shipThruWall = 20 # How much of the ship needs to go thru the wall to activate
    wallOffset = 6
    if redShip.exactPos[0] < 0-wallOffset-shipThruWall:
        redShip.exactPos[0] = WIDTH-wallOffset-52+shipThruWall # 52 is ships height
    elif redShip.exactPos[0] > WIDTH-wallOffset-52+shipThruWall:
        redShip.exactPos[0] = 0-wallOffset-shipThruWall
    if redShip.exactPos[1] < 0-wallOffset-shipThruWall:
        redShip.exactPos[1] = HEIGHT-wallOffset-56+shipThruWall # 56 is ships width
    elif redShip.exactPos[1] > HEIGHT-wallOffset-56+shipThruWall:
        redShip.exactPos[1] = 0-wallOffset-shipThruWall

    goalAngle = rot_to_blueShip(blueShip, redShip)

    metGoalAngle = check_close_meteors(meteors, redShip)
    if metGoalAngle != None:
        goalAngle = metGoalAngle

    bulGoalAngle = check_close_bullets(blueShip.bullets, redShip)
    if bulGoalAngle != None:
        goalAngle = bulGoalAngle

    realRedShipRot = -redShip.rotation
    realRedShipRot = changeShipRotReturn(0, realRedShipRot)
    rotDirection = changeShipRotReturn(-goalAngle, realRedShipRot)
    
    if rotDirection > 0 and rotDirection < 180:
        changeShipRot(rotChange, redShip)
    else:
        changeShipRot(-rotChange, redShip)

    redShip.exactPos[0] -= speed * math.cos((redShip.rotation+270) * 3.1415 / 180)
    redShip.exactPos[1] += speed * math.sin((redShip.rotation+270) * 3.1415 / 180)
    redShip.pos.x = int(redShip.exactPos[0])
    redShip.pos.y = int(redShip.exactPos[1])


def rot_to_blueShip(blueShip, redShip):
    blueShipRelativePos = [blueShip.exactPos[0]-redShip.exactPos[0], blueShip.exactPos[1]-redShip.exactPos[1]]
    blueLenght = math.sqrt(blueShipRelativePos[0]**2 + blueShipRelativePos[1]**2)
    skalarProduct = 0
    if blueShip.exactPos[0]-redShip.exactPos[0] < 0:
        skalarProduct = blueShipRelativePos[1]
    else:
        skalarProduct = -blueShipRelativePos[1]

    degrees = math.degrees(math.acos(skalarProduct/blueLenght))
    
    if blueShip.exactPos[0]-redShip.exactPos[0] >= 0:
        print(degrees)
        return degrees
    else:
        print(degrees+180)
        return degrees+180


def check_close_meteors(meteors, redShip):
    redShipPos = [redShip.exactPos[0] + 28, redShip.exactPos[1] + 26]
    goalAngle = None # Should = angle to blueShip
    for meteor in meteors:
        meteorPos = [meteor[3][0] + 32, meteor[3][1] + 32]
        distanceToMeteor = [meteorPos[0] - redShipPos[0], meteorPos[1] - redShipPos[1]]
        if distanceToMeteor[0] < 280 and distanceToMeteor[0] > -280 and distanceToMeteor[1] < 280 and distanceToMeteor[1] > -280:
            goalAngle = meteor[1] - 135
            
    return goalAngle


def check_close_bullets(bullets, redShip):
    redShipPos = [redShip.exactPos[0] + 28, redShip.exactPos[1] + 26]
    goalAngle = None # Should = angle to blueShip
    for bullet in bullets:
        bulletPos = [bullet[0] + 32, bullet[1] + 32]
        distanceToMeteor = [bulletPos[0] - redShipPos[0], bulletPos[1] - redShipPos[1]]
        if distanceToMeteor[0] < 280 and distanceToMeteor[0] > -280 and distanceToMeteor[1] < 280 and distanceToMeteor[1] > -280:
            goalAngle = bullet[1] - 135
            
    return goalAngle
    