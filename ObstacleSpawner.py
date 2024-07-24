import pygame
import random

class ObstacleSpawner:

    def __init__(self, screen, player1):
        self.obstaclesListRight = []
        self.obstacleListLeft = []
        self.obstacleLocation = []
        self.obstacleWidth = 50
        self.obstacleHeight = 50
        self.obstacleRectArraylistStorage = []

        #Obstacle default location

        self.obstacleVelocity = 6

        #Get the screen from the parameter, define the parameter in the main class
        self.screen = screen
        self.player1 = player1

        #Obstacle Rect

    def generateObstacle(self):
        # create random obstacle
        #Spawning from the top right
        obstacleRNGRightX = random.randint(799, 1600)
        obstacleRNGRightY = random.uniform(-799, 799)
        # create valid random coords
        """"
        while (
                    self.player1.playerXCoord - self.player1.playerAntiSpawnRadius < self.obstacleRNGX < self.player1.playerXCoord + self.player1.playerAntiSpawnRadius
                and self.player1.playerYCoord - self.player1.playerAntiSpawnRadius < self.obstacleRNGY < self.player1.playerYCoord + self.player1.playerAntiSpawnRadius):
            self.obstacleRNGX = random.randint(799, 1600)
            self.obstacleRNGY = random.randint(0, 1600)
        """
        # record coord information in obstacles[]

        self.obstaclesListRight.append((obstacleRNGRightX, obstacleRNGRightY))

        #Top left
        obstacleRNGLeftX = random.uniform(0, -799)
        obstacleRNGLeftY = random.uniform(-799, 799)

        self.obstacleListLeft.append((obstacleRNGLeftX, obstacleRNGLeftY))

    def drawObstacle(self):

        #Len means the size of the list
        #Draw right side
        for i in range(len(self.obstaclesListRight)):
            #DO NOT MAKE THIS A SELF VALUE, THIS OBSTACLE IS LIMITED TO EACH ITERATION.
            obstacleRect = pygame.draw.rect(self.screen, (255, 255, 255),
                                            (*self.obstaclesListRight[i], self.obstacleWidth, self.obstacleHeight))

            self.obstacleRectArraylistStorage = []
            self.obstacleRectArraylistStorage.append(obstacleRect)

            #Unpack obstacles into obsX and obsY

            obsX, obsY = self.obstaclesListRight[i]
            obsX -= self.obstacleVelocity
            obsY += self.obstacleVelocity

            #Repack obstacles back into the array

            # Update the obstacle at the current index
            self.obstaclesListRight[i] = (obsX, obsY)

        #Draw left side
        for i in range(len(self.obstacleListLeft)):
            # DO NOT MAKE THIS A SELF VALUE, THIS OBSTACLE IS LIMITED TO EACH ITERATION.
            obstacleRect = pygame.draw.rect(self.screen, (255,255, 255),
                                            (*self.obstacleListLeft[i], self.obstacleWidth, self.obstacleHeight))

            self.obstacleRectArraylistStorage = []
            self.obstacleRectArraylistStorage.append(obstacleRect)

            # Unpack obstacles into obsX and obsY

            obsX, obsY = self.obstacleListLeft[i]
            obsX += self.obstacleVelocity
            obsY += self.obstacleVelocity

            # Repack obstacles back into the array

            # Update the obstacle at the current index
            self.obstacleListLeft[i] = (obsX, obsY)


    #public boolean method
    def checkForObstacleCollisions(self):
        for i in range(len(self.obstaclesListRight)):
            gameVersionObsX, gameVersionObsY = self.obstaclesListRight[i]
            gameVersionObstacle = pygame.draw.rect(self.screen, (255, 255, 255),
                                                   (gameVersionObsX, gameVersionObsY,
                                                    self.obstacleWidth,
                                                    self.obstacleHeight))

            if self.player1.controllablePlayer.colliderect(gameVersionObstacle):
                #Remove obstacle from array after player hits it
               self.obstaclesListRight.pop(i)
               return True

        for i in range(len(self.obstacleListLeft)):
            gameVersionObsX, gameVersionObsY = self.obstacleListLeft[i]
            gameVersionObstacle = pygame.draw.rect(self.screen, (255, 255, 255),
                                                   (gameVersionObsX, gameVersionObsY,
                                                    self.obstacleWidth,
                                                    self.obstacleHeight))

            if self.player1.controllablePlayer.colliderect(gameVersionObstacle):
                #Remove obstacle from array after player hits it
               self.obstacleListLeft.pop(i)
               return True


        return False

    def removeObstaclesBeyondBorders(self):
        # Remove obstaclesListRight elements
        for i in reversed(range(len(self.obstaclesListRight))):

            obsX, obsY = self.obstaclesListRight[i]
            if obsX > 1600 or obsY > 799:
                self.obstaclesListRight.pop(i)
                #print("removed from obstaclesListRight")

        # Remove obstacleListLeft elements
        for i in reversed(range(len(self.obstacleListLeft))):
            obsX, obsY = self.obstacleListLeft[i]
            if obsX < -799 or obsY > 799:
                self.obstacleListLeft.pop(i)
                #print("removed from obstacleListLeft")
    def deleteAllObstacles(self):
        for i in reversed(range(len(self.obstaclesListRight))):
            self.obstaclesListRight.pop(i)
        for i in reversed(range(len(self.obstacleListLeft))):
            self.obstacleListLeft.pop(i)




























