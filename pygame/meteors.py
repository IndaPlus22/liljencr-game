import pygame
import math

# Holds meteors where meteor[0] is its rect and [1] is its moving direction and [2] is its rendered rotation and [3] is its exact position
meteors = []
meteorSpeed = 10

def set_meteors(data):
    global meteors
    meteors = data

def rot_center(image, rect, angle):  # Rotate image around center, common pygame code
    rotImage = pygame.transform.rotate(image, angle)
    rotRect = rotImage.get_rect(center=rect.center)
    return rotImage, rotRect

def draw_meteors(win, texture):
    for meteor in meteors:
        roti, rotr = rot_center(texture, meteor[0], meteor[2])
        win.blit(roti, rotr)

def check_meteor_collision(blueShip, redShip):
    for meteor in meteors:
        blueDistance = [meteor[3][0]+32 - (blueShip.exactPos[0]+28), meteor[3][1]+32 - (blueShip.exactPos[1]+26)]
        if blueDistance[0] < 50 and blueDistance[0] > -50 and blueDistance[1] < 50 and blueDistance[1] > -50: # Hitbox is circular, radius 50
            return "blue"
        
        redDistance = [meteor[3][0]+32 - (redShip.exactPos[0]+28), meteor[3][1]+32 - (redShip.exactPos[1]+26)]
        if redDistance[0] < 50 and redDistance[0] > -50 and redDistance[1] < 50 and redDistance[1] > -50: # Hitbox is circular, radius 64
            return "red"
    
    return None


def move_meteors(WIDTH, HEIGHT):
    for meteor in meteors:
        meteor[3][0] -= meteorSpeed * math.cos((meteor[1]+270) * 3.1415 / 180)
        meteor[3][1] += meteorSpeed * math.sin((meteor[1]+270) * 3.1415 / 180)
        meteor[0].x = int(meteor[3][0])
        meteor[0].y = int(meteor[3][1])

        meteor[2] += 6 # Update visual rotation of meteor

        # Meteors that go of screen will show up on the other side: (It has some offsets because of the pos being the top left corner of the meteor)
        meteorThruWall = 26 # How much of the meteor needs to go thru the wall to activate
        wallOffset = 6
        if meteor[3][0] < 0-wallOffset-meteorThruWall:
            meteor[3][0] = WIDTH-wallOffset-64+meteorThruWall # 64 is meteors height
        elif meteor[3][0] > WIDTH-wallOffset-64+meteorThruWall:
            meteor[3][0] = 0-wallOffset-meteorThruWall
        if meteor[3][1] < 0-wallOffset-meteorThruWall:
            meteor[3][1] = HEIGHT-wallOffset-64+meteorThruWall # 64 is meteors width
        elif meteor[3][1] > HEIGHT-wallOffset-64+meteorThruWall:
            meteor[3][1] = 0-wallOffset-meteorThruWall
    

