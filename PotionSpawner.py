import pygame
import random
class PotionSpawner():


    def __init__(self, screen, player1):
        self.idk = 0
        self.player1 = player1
        self.screen = screen
        #Methods can only detect variables that are inside the __init__ function when outside of their respective methods
        #Declaring a method outside the init is unreadable to other methods
        self.PotionList = []
        self.TrianglePotionList = []

        self.PotionWidth = 50
        self.PotionHeight = 50

    def spawnPotion(self):
        self.potionRNGX = random.randint(1, 799)
        self.potionRNGY = random.randint(1, 799)
        # create valid random coords
        while (
                self.player1.playerXCoord - self.player1.playerAntiSpawnRadius < self.potionRNGX < self.player1.playerXCoord + self.player1.playerAntiSpawnRadius
                and self.player1.playerYCoord - self.player1.playerAntiSpawnRadius < self.potionRNGY < self.player1.playerYCoord + self.player1.playerAntiSpawnRadius):
            self.potionRNGX = random.randint(1, 799)
            self.potionRNGY = random.randint(1, 799)
        # record coord information in obstacles[]
        self.PotionList.append((self.potionRNGX, self.potionRNGY))

    def spawnTrianglePotion(self):
        # create valid random coords within the main screen 800x800
        TrianglePotionRNGX = random.randint(1, 799)
        TrianglePotionRNGY = random.randint(1, 799)

        # record coord information in obstacles[]
        self.TrianglePotionList.append((TrianglePotionRNGX, TrianglePotionRNGY))

    def checkForPotionCollisions(self):
        for i in range(len(self.PotionList)):

            xhv1, yhv1 = self.PotionList[i]
            xhv2, yhv2 = xhv1 + 200 / 3, yhv1 + 100 / 3
            xhv3, yhv3 = xhv1 + 250 / 3, yhv1 + 50 / 3
            xhv4, yhv4 = xhv1 + 300 / 3, yhv1 + 100 / 3
            xhv5, yhv5 = xhv1 + 200 / 3, yhv1 + 200 / 3
            xhv6, yhv6 = xhv1 + 100 / 3, yhv1 + 100 / 3
            xhv7, yhv7 = xhv1 + 150 / 3, yhv1 + 50 / 3
            heart_points = [(xhv2, yhv2), (xhv3, yhv3), (xhv4, yhv4), (xhv5, yhv5), (xhv6, yhv6), (xhv7, yhv7)]

            potionRect = pygame.draw.polygon(self.screen, (255, 0, 0), (heart_points))

            if self.player1.controllablePlayer.colliderect(potionRect):
                #Remove obstacle from array after player hits it
               reversed(self.PotionList.pop(i))
               return True

        return False
    def checkForTrianglePotionCollisions(self):
        for i in range(len(self.TrianglePotionList)):
            triangleVerticeX1, triangleVerticeY1 = self.TrianglePotionList[i]
            triangleVerticeX2, triangleVerticeY2 = (triangleVerticeX1 + 25), (triangleVerticeY1 - 50)
            triangleVerticeX3, triangleVerticeY3 = (triangleVerticeX1 + 50), (triangleVerticeY1 - 0)

            vertice1 = triangleVerticeX1, triangleVerticeY1
            vertice2 = triangleVerticeX2, triangleVerticeY2
            vertice3 = triangleVerticeX3, triangleVerticeY3

            trianglePotionRect = pygame.draw.polygon(self.screen, (235, 232, 52),
                                (vertice1, vertice2, vertice3))

            if self.player1.controllablePlayer.colliderect(trianglePotionRect):
                #Remove obstacle from array after player hits it
               self.TrianglePotionList.pop(i)
               return True

        return False

    def drawAllPotions(self):
        #Draw health potion



        for i in range(len(self.PotionList)):

            xhv1, yhv1 = self.PotionList[i]
            xhv2, yhv2 = xhv1 + 200/3, yhv1 + 100/3
            xhv3, yhv3 = xhv1 + 250/3, yhv1 + 50/3
            xhv4, yhv4 = xhv1 + 300/3, yhv1 + 100/3
            xhv5, yhv5 = xhv1 + 200/3, yhv1 + 200/3
            xhv6, yhv6 = xhv1 + 100/3, yhv1 + 100/3
            xhv7, yhv7 = xhv1 + 150/3, yhv1 + 50/3
            heart_points = [(xhv2, yhv2), (xhv3, yhv3), (xhv4, yhv4), (xhv5, yhv5), (xhv6, yhv6), (xhv7, yhv7)]


            pygame.draw.polygon(self.screen, (255, 0, 0), (heart_points))
        #Draw triangle potion
        for i in range(len(self.TrianglePotionList)):
            #Unpack original x,y, then create the vertices
            triangleVerticeX1, triangleVerticeY1 = self.TrianglePotionList[i]
            triangleVerticeX2, triangleVerticeY2 = (triangleVerticeX1 + 25), (triangleVerticeY1 - 50)
            triangleVerticeX3, triangleVerticeY3 = (triangleVerticeX1 + 50), (triangleVerticeY1 - 0)

            vertice1 = triangleVerticeX1, triangleVerticeY1
            vertice2 = triangleVerticeX2, triangleVerticeY2
            vertice3 = triangleVerticeX3, triangleVerticeY3

            pygame.draw.polygon(self.screen, (235, 232, 52),
                             (vertice1, vertice2, vertice3))

    def deleteAllPotions(self):
        for i in range(len(self.TrianglePotionList)):
            self.TrianglePotionList.pop(i)
        for i in reversed(range(len(self.PotionList))):
            self.PotionList.pop(i)









