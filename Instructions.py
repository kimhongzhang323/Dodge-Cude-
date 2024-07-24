import pygame
class Instructions:

    def __init__(self, game1):
        self.ScreenWidth = game1.ScreenWidth
        self.ScreenHeight = game1.ScreenHeight
        self.font = pygame.font.SysFont('Arial', 64)
        self.fontSize = 12
        self.fontColour = (255, 3, 3)
        self.pos = (0, 0)



# Example usage:
pygame.init()
game1 = pygame.display.set_mode((800, 600))
instructions = Instructions(game1)

