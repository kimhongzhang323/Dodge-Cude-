import pygame
from pygame import mixer

class Player:
    def __init__(self, screen):
        self.playerVelocity = 5
        self.playerXCoord = 400
        self.playerYCoord = 400
        self.playerWidth = 5
        self.playerHeight = 5
        self.playerCollided = False
        self.playerAntiSpawnRadius = 50
        self.Hearts = 3
        self.trianglePotionsCollected = 0
        self.playerCollidedWithObstacle = False

        self.screen = screen
        self.controllablePlayer = pygame.draw.rect(self.screen, (200, 23, 255), (self.playerXCoord, self.playerYCoord, self.playerWidth, self.playerHeight))

    def movePlayer(self, keys):
        test = None

    def drawPlayer(self):
        self.controllablePlayer = pygame.draw.rect(self.screen, (200, 23, 255), (self.playerXCoord, self.playerYCoord, self.playerWidth, self.playerHeight))

    def checkForBorderCollision(self, screenWidth, screenHeight, keys):
        if keys[pygame.K_w]:
            self.playerYCoord -= self.playerVelocity
        if keys[pygame.K_a]:
            self.playerXCoord -= self.playerVelocity
        if keys[pygame.K_s]:
            self.playerYCoord += self.playerVelocity
        if keys[pygame.K_d]:
            self.playerXCoord += self.playerVelocity


        # Border checkers
        #Do not turn oldPlayer into a self, this keeps it constantly updated everytime self.player moves. Only update it with every iteration
        oldPlayerX = self.playerXCoord - 5
        oldPlayerY = self.playerYCoord - 5

        # Bottom side
        if self.playerXCoord and self.playerYCoord >= screenWidth:
            self.playerYCoord = oldPlayerY
            #print("s key has been disabled")
            return True
        # Top side
        if self.playerXCoord and self.playerYCoord <= -1:
            self.playerYCoord = oldPlayerY + 10
            #print("w key has been disabled")
            return True

        # Left side
        if self.playerXCoord <= -1:
            self.playerXCoord = oldPlayerX + 10
            #print("a key has been disabled")
            return True
        # Right side
        if self.playerXCoord >= screenWidth:
            self.playerXCoord = oldPlayerX
            #print("d key has been disabled")
            return True

    def transformIntoTriangleSprite(self):
        print("To be continued")