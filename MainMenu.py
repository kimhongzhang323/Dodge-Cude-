import pygame
import sys
import os

from Game import Game
from pygame import mixer
from Player import Player
from ObstacleSpawner import ObstacleSpawner
from PotionSpawner import PotionSpawner
from Leaderboard import SaveLoadSystem

#Referenced from GeekForGeeks
#Code alligned for tidyness by ChatGPT

class MainMenu:
    def __init__(self):
        self.test = 0
        self.returnedToMainMenu = False
        self.mainMenuON = True

    def load_Effects(self, effectName):
        script_dir = os.path.dirname(__file__)
        rel_path = os.path.join("GameSoundEffects", effectName)
        # Absolute path
        abs_file_path = os.path.join(script_dir, rel_path)
        pygame.mixer.Sound(abs_file_path)
        return pygame.mixer.Sound(abs_file_path)

    def playEffects(self, effectName):
        self.load_Effects(effectName).play()

    def startClicking(self):
        self.load_Effects("clicking.mp3")
        self.playEffects("clicking.mp3")

    def loadImage(self, imageName, sizeX, sizeY):
        script_dir = os.path.dirname(__file__)
        rel_path = os.path.join("Images", imageName)
        # Absolute path
        abs_file_path = os.path.join(script_dir, rel_path)

        # Load Background image
        background_image = pygame.image.load(abs_file_path)
        # Scale the image to match the screen size
        background_image = pygame.transform.scale(background_image, (sizeX, sizeY))
        return background_image

    def startMainMenu(self):
        #Construct the classes
        screen = pygame.display.set_mode((800, 800))
        #mixer.music.load('C:\\Users\\USER\\Music\\dbzOp.mp3')
        #mixer.music.set_volume(0.2)
        #mixer.music.play()

     # Load Background pattern image
     #    background_pattern = pygame.image.load(r'C:\Users\DELL\Downloads\background.png')
     # # Scale the image to match the screen size
     #    background_pattern = pygame.transform.scale(background_pattern, (800,800))

        player1 = Player(screen)
        obstacleSpawner1 = ObstacleSpawner(screen, player1)
        potionSpawner1 = PotionSpawner(screen, player1)
        saveLoadSystem1 = SaveLoadSystem(self)
        mainMenu1 = MainMenu()
        game1 = Game(player1, obstacleSpawner1, potionSpawner1, saveLoadSystem1, mainMenu1)

        pygame.init()
        screen1 = pygame.display.set_mode((800, 800))

        InstructionTurnedOn = False
        LeaderboardTurnedOn = False

        #1) Implement outline(White Box surrounding bg)
        #Default color is white
        color = (200, 200, 200)
        color_light = (200, 200, 200)
        color_dark = (50, 50, 50)
        color_LightRed = (200, 0, 0)
        color_DarkRed = (100, 0, 0)
        color_DarkBlue = (0, 0, 100)

        color_black = (0,0,0)

        width = screen1.get_width()
        height = screen1.get_height()

        buttonfont = pygame.font.SysFont('Agency FB', 35)
        titlefont = pygame.font.SysFont('Haettenschweiler',85 )
        playfont = pygame.font.SysFont('Haettenschweiler' , 60 )
        leaderboardfont = pygame.font.SysFont('Haettenschweiler' , 55 )
        instructionsfont = pygame.font.SysFont('Haettenschweiler', 72)
        backfont = pygame.font.SysFont('Haettenschweiler' , 50)

        #Window 1 Text
        titleText = titlefont.render('DODGE CUBE', True, (0, 0, 0))
        StartPlayText = playfont.render('Start', True, (255,255,255))
        InstructionText = leaderboardfont.render('Instructions', True, (255,255,255))
        ExitText = playfont.render('Exit', True, (255,255,255))
        LeaderboardText = leaderboardfont.render('Leaderboard', True, (255,255,255))

        backText = backfont.render("Back", True, (255,255,255))

        #Window 2 Text
        posX = (width * 1/8)
        posY = (height * 1/8)
        position = posX, posY

        #Pygame cannot utilise \n, youll need to manually separate them
        instructionContent1 = instructionsfont.render("Instructions", True, (0,0,0))
        instructionContent2 = buttonfont.render("1) WASD to move", True, (0,0,0))
        instructionContent3 = buttonfont.render("2) Heart potion to heal", True, (0,0,0))
        instructionContent31 = buttonfont.render("3) Triangle potion to break blocks", True, (0,0,0))
        instructionContent4 = buttonfont.render("4) M to mute music", True, (0,0,0))
        instructionContent5 = buttonfont.render("5) L to unmute music", True, (0,0,0))
        instructionContent6 = buttonfont.render("6) P to pause game", True, (0,0,0))
        instructionContent7 = buttonfont.render("7) O to unpause game", True, (0,0,0))

        saveLoadSystem1.load_numbers_from_file()
        saveLoadSystem1.save_and_display_top5(game1.finalScore)
        saveLoadSystem1.mainMenuLog()

        score1 = buttonfont.render("1) " + str(saveLoadSystem1.num1), True, (255,255,255))
        score2 = buttonfont.render("2) " + str(saveLoadSystem1.num2), True, (255,255,255))
        score3 = buttonfont.render("3) " + str(saveLoadSystem1.num3), True, (255,255,255))
        score4 = buttonfont.render("4) " + str(saveLoadSystem1.num4), True, (255,255,255))
        score5 = buttonfont.render("5) " + str(saveLoadSystem1.num5), True, (255,255,255))


        while True:
            for pygameEvent in pygame.event.get():
                if pygameEvent.type == pygame.QUIT:
                    pygame.quit()

                screen1.fill((255, 255, 255))
                screen1.blit(self.loadImage("background.png", 800,800), (0, 0))  # Draw the background image

                userMouse = pygame.mouse.get_pos()

                #NOTE: minus makes graphics display up while plus makes graphics display downwards

                if self.mainMenuON:
                    #Title Text
                    screen1.blit(titleText, (width/2-150, height/2 - 265))
                    #Draw Box + Text 1: Start
                    if width / 2 - 100 <= userMouse[0] <= width / 2 + 150 and height / 2 - 70 <= userMouse[1] <= height / 2 - 30:
                        pygame.draw.rect(screen1, color_light, [width / 2 - 130, height / 2 - 90, 250, 60])
                        #Initialize the game when button is clicked in the play area
                        if pygameEvent.type == pygame.MOUSEBUTTONDOWN:

                                game1.start()
                                #while game1.getRunningStatus() == True:
                                #    if(game1.getRunningStatus() == False):
                                #        break

                    else:
                        pygame.draw.rect(screen1, color_black, [width / 2 - 130, height / 2 - 90, 250, 60])

                    screen1.blit(StartPlayText, (width / 2 - 57, height / 2 - 95))


                    # Draw Box + Text 2: Instructions
                    if width / 2 - 75 <= userMouse[0] <= width / 2 + 150 and height / 2 + 0 <= userMouse[1] <= height / 2 + 46:
                        pygame.draw.rect(screen1, color_light, [width / 2 - 130, height / 2 - 0, 250, 60])
                        if pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                            self.startClicking()

                            InstructionTurnedOn = True
                            self.mainMenuON = False
                    else:
                        pygame.draw.rect(screen1, color_black, [width / 2 - 130, height / 2 - 0, 250, 60])

                    screen1.blit(InstructionText, (width / 2 - 110, height / 2 - 3))

                    #3) Leaderboard (2blocks under the exit)
                    if width / 2 - 75 <= userMouse[0] <= width / 2 + 105 and height / 2 + 90 <= userMouse[1] <= height / 2 + 150:
                        pygame.draw.rect(screen1, color_light, [width / 2 - 130, height / 2 + 90, 250, 60])

                        # If event = mouseClick Do
                        if pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                            LeaderboardTurnedOn = True
                            self.startClicking()
                    else:
                        pygame.draw.rect(screen1, color_black, [width / 2 - 130, height / 2 + 90, 250, 60])

                    screen1.blit(LeaderboardText, (width / 2 - 115, height / 2 + 90))

                    # Draw Box + Text 4: Exit
                    if width / 2 - 75 <= userMouse[0] <= width / 2 + 105 and height / 2 + 180 <= userMouse[
                        1] <= height / 2 + 320:
                        pygame.draw.rect(screen1, color_light, [width / 2 - 130, height / 2 + 180, 250, 60])

                        # If event = mouseClick Do:
                        if pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                            self.startClicking()
                            pygame.quit()
                    else:
                        pygame.draw.rect(screen1, color_black, [width / 2 - 130, height / 2 + 180, 250, 60])

                    screen1.blit(ExitText, (width / 2 - 42, height / 2 + 177))


                #Instruction Screen
                if InstructionTurnedOn:
                    self.mainMenuON = False

                    screen1.fill((255, 255, 255))
                    # Load and scale the background image
                    # background_image = pygame.image.load(r'C:\Users\DELL\Downloads\blackbg.png')
                    # background_image = pygame.transform.scale(background_image, (800, 800))

                    # Blit the background image onto the screen
                    screen1.blit(self.loadImage("blackbg.png", 800,800), (0, 0))  # Draw the background image

                    #Inner rect
                    pygame.draw.rect(screen1, (100,100,100), [width / 2 - 240, height / 2 - 300, 500, 600])

                    # Load and scale the background image
                    # background_image = pygame.image.load(r'C:\Users\DELL\Downloads\whitebg.png')
                    # background_image = pygame.transform.scale(background_image, (500, 600))

                    # Blit the background image onto the screen
                    screen1.blit(self.loadImage("whitebg.png", 500, 600), (width / 2 - 240, height / 2 - 300))

                    screen1.blit(instructionContent1, (width / 2 - 120, height / 2 - 260))
                    screen1.blit(instructionContent2, (width / 2 - 220, height / 2 - 150))
                    screen1.blit(instructionContent3, (width / 2 - 220, height / 2 - 100))
                    screen1.blit(instructionContent31, (width / 2 - 220, height / 2 - 50))
                    screen1.blit(instructionContent4, (width / 2 - 220, height / 2 - 0))
                    screen1.blit(instructionContent5, (width / 2 - 220, height / 2 + 50))
                    screen1.blit(instructionContent6, (width / 2 - 220, height / 2 + 100))
                    screen1.blit(instructionContent7, (width / 2 - 220, height / 2 + 150))

                    # Back button
                    button_width = 150
                    button_height = 50
                    button_x = width / 2 - 65
                    button_y = height / 2 + 235

                    if button_x <= userMouse[0] <= button_x + button_width and button_y <= userMouse[
                        1] <= button_y + button_height:
                        pygame.draw.rect(screen1, color_light, [button_x, button_y, button_width, button_height])
                        if pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                            self.mainMenuON = True

                            InstructionTurnedOn = False
                            self.startClicking()
                    else:
                        pygame.draw.rect(screen1, color_black, [button_x, button_y, button_width, button_height])

                    screen1.blit(backText, (width / 2 - 30, height / 2 + 230))

                if LeaderboardTurnedOn:
                    self.mainMenuON = False
                    screen1.fill((0, 25, 50))

                    # Load and scale the background image
                    # background_image = pygame.image.load(r'C:\Users\DELL\Downloads\blackbg.png')
                    # background_image = pygame.transform.scale(background_image, (800, 800))

                    # Blit the background image onto the screen
                    screen1.blit(self.loadImage("blackbg.png", 800, 800), (0, 0))  # Draw the background image

                    pygame.draw.rect(screen1, color_DarkBlue, [width / 2 - 240, height / 2 - 300, 500, 600])

                    # Load and scale the background image
                    # background_image = pygame.image.load(r'C:\Users\DELL\Downloads\grey.png')
                    # background_image = pygame.transform.scale(background_image, (500, 600))

                    # Blit the background image onto the screen
                    screen1.blit(self.loadImage("grey.png",500,600), (width / 2 - 240, height / 2 - 300))

                    leaderboard_color = (0,0,0)
                    leaderboard_text_rendered = leaderboardfont.render('Leaderboard', True, (0,0,0))
                    screen1.blit(leaderboard_text_rendered, (width/2 - 90, height /2 - 280), )

                    # Underline score value
                    score_heights = [height / 2 - 200, height / 2 - 125, height / 2 - 50, height / 2 + 25, height / 2 + 100]
                    scores = [score1, score2, score3, score4, score5]

                    for i in range(len(scores)):
                        # Draw the score value
                        screen1.blit(scores[i], (width / 2 - 220, score_heights[i]))

                        # Underline the score value
                        underline_start = (width / 2 - 220, score_heights[i] + scores[i].get_height())
                        underline_end = (
                        width / 2 - 220 + scores[i].get_width(), score_heights[i] + scores[i].get_height())
                        pygame.draw.line(screen1, (0, 0, 0), underline_start, underline_end, 2)

                    screen1.blit(score1, (width / 2 - 220, height / 2 - 200))
                    screen1.blit(score2, (width / 2 - 220, height / 2 - 125))
                    screen1.blit(score3, (width / 2 - 220, height / 2 - 50))
                    screen1.blit(score4, (width / 2 - 220, height / 2 + 25))
                    screen1.blit(score5, (width / 2 - 220, height / 2 + 100))

                # Back button
            if LeaderboardTurnedOn:
                button_width = 115
                button_height = 50
                button_x = width / 2 - 45
                button_y = height / 2 + 220

                if button_x <= userMouse[0] <= button_x + button_width and button_y <= userMouse[
                    1] <= button_y + button_height:
                    pygame.draw.rect(screen1, color_light, [button_x, button_y, button_width, button_height])
                    if pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                        LeaderboardTurnedOn = False
                        self.mainMenuON = True
                        self.startClicking()
                else:
                    pygame.draw.rect(screen1, color_black, [button_x, button_y, button_width, button_height])

                screen1.blit(backText, (width / 2 - 25, height / 2 + 215))

            pygame.display.update()