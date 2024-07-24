import pygame
import random
import time
import json
import os

from pygame import mixer
from Player import Player
from ObstacleSpawner import ObstacleSpawner
from PotionSpawner import PotionSpawner
from Leaderboard import SaveLoadSystem
#from Instructions import Instructions


pygame.init()
class Game():


    def __init__(self , playerHere, obstaclespawnerHere, potionspawnerHere, saveLoadSystemHere, mainMenuHere):
        # Default values
        self.gameplayerCollided = False
        self.playerCollidedWithBorder = False
        self.triangleDurationText = 0
        self.score = 0
        self.highscores = []
        self.gameOver = False
        self.finalScore = 0

        self.scoreLogged = False

        #Construct the class
        self.playerObj = playerHere
        self.obstacleObj = obstaclespawnerHere
        self.potionObj = potionspawnerHere
        self.saveLoadSystemObj = saveLoadSystemHere
        self.mainMenu = mainMenuHere
        print("Current file path:", os.path.abspath(__file__))

    def startClicking(self):
        self.load_Effects("clicking.mp3")
        self.playEffects("clicking.mp3")


    def load_music(self, musicName):
        script_dir = os.path.dirname(__file__)
        rel_path = os.path.join("GameSoundEffects", musicName)
        #Absolute path
        abs_file_path = os.path.join(script_dir, rel_path)
        pygame.mixer.music.load(abs_file_path)

    def playMusic(self, musicName):
        if __name__ == "__main__":
            pygame.mixer.init()
            self.load_music(musicName)
            pygame.mixer.music.play()

    def load_Effects(self, effectName):
        script_dir = os.path.dirname(__file__)
        rel_path = os.path.join("GameSoundEffects", effectName)
        # Absolute path
        abs_file_path = os.path.join(script_dir, rel_path)
        pygame.mixer.Sound(abs_file_path)
        return pygame.mixer.Sound(abs_file_path)

    def playEffects(self, effectName):
        self.load_Effects(effectName).play()


    def start(self):

        while True:
            #mixer.music.load('C:\\Users\\USER\\PycharmProjects\\PurePacman\\gameBgMusic.mp3')
            self.load_music("")
            self.playMusic("")


            mixer.music.set_volume(0.5)
            mixer.music.play()

            ScreenWidth = 800
            ScreenHeight = 800
            # Initialize screen and title
            screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

            color_light = (170, 170, 170)
            color_dark = (100, 100, 100)

            pygame.display.set_caption("Game title")
            clock1 = pygame.time.Clock()
            tickCounter = 0
            timeInSeconds = 0

            # Font
            font = pygame.font.SysFont('Corbel', 35)
            gamePaused = False
            gameUnpaused = False
            gameRestarted = False
            gameplayerCollided = False
            replayed = False


            #Construct the classes


            #instructions1 = Instructions(screen)

            running = True
            while running:
               #Scoreboard



                newTime = str(float(timeInSeconds))
                timeText = "Time survived: "
                printTime = font.render(timeText + newTime, True, (255, 255, 255))

                strScore = str(self.score)
                scoreText = "Score: "
                printScore = font.render(scoreText + strScore, True, (255, 255, 255))

                heartText = "Lives: " + str(self.playerObj.Hearts) + "/3"
                printHearts = font.render(heartText, True, (255,255,255))

                #instructions1.blit_textMethod(screen, "font")


               #Leaderboard

                keys = pygame.key.get_pressed()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif keys[pygame.K_p]:
                        gamePaused = True
                        mixer.music.pause()
                    elif keys[pygame.K_o]:
                        gamePaused = False
                        mixer.music.unpause()
                    userMouse = pygame.mouse.get_pos()


                    # Player class instanced!
                    # self.playerObj = Player(screen)

                #Game unpaused
                if (gamePaused == False):
                    # Limit the frames per second
                    clock1.tick(60)
                    tickCounter += 1

                    # Every time tickcounter hits 1e+9 ticks, seconds++
                    # Corrected: 100 ticks make a second!
                    if tickCounter % 60 == 0:
                        timeInSeconds += 1

                    if tickCounter % 1 == 0:
                        self.score += 1

                    triangleText = "Triangle form: "
                    printTriangle = font.render(triangleText + str(self.triangleDurationText) + "/5", True, (255, 255, 255))

                    #player controls
                    self.playerObj.movePlayer(keys)
                    if (keys[pygame.K_o]):
                        gamePaused = False
                    if keys[pygame.K_r]:
                        gameRestarted = True
                    if keys[pygame.K_m]:
                        mixer.music.pause()
                    if keys[pygame.K_l]:
                        mixer.music.unpause()

                    screen.fill(((0,0,0)))
                    self.playerObj.drawPlayer()

                    if (tickCounter % 10 and self.gameOver == False) == 0:
                        self.obstacleObj.generateObstacle()

                    self.obstacleObj.drawObstacle()
                    self.obstacleObj.removeObstaclesBeyondBorders()

                    # create potions every 10 second(1000ticks)
                    #Health potions
                    if tickCounter % 500 == 0:
                        self.potionObj.spawnPotion()
                    #Triangle Potion
                    if tickCounter % 2000 == 0:
                        self.potionObj.spawnTrianglePotion()
                    self.potionObj.drawAllPotions()

                    #Remove triangle effect after 5 seconds
                    #if tickCounter % 500 == 0:
                    #    self.playerObj.trianglePotionsCollected = 0

                    #Potion collision
                    if self.potionObj.checkForPotionCollisions():
                        if not self.playerObj.Hearts >= 3:
                            self.playerObj.Hearts += 1
                            #potionSound = mixer.Sound('C:\\Users\\USER\\Music\\mafiacitylevelup.mp3')
                            self.load_Effects(".")
                            self.playEffects(".")

                        #Hearts full
                        else:
                            #fullHeartsAlready = mixer.Sound('C:\\Users\\USER\\Music\\bruh.mp3')
                            #fullHeartsAlready.play()

                            self.load_Effects(".")

                    if self.potionObj.checkForTrianglePotionCollisions():
                        #Max triangle limits is 1
                        if self.playerObj.trianglePotionsCollected < 2:
                            # trianglePotionSound = mixer.Sound('C:\\Users\\USER\\Music\\5secondsAudio.mp3')
                            # trianglePotionSound.play()
                            self.load_Effects(".")
                            self.playEffects(".")

                            self.playerObj.trianglePotionsCollected += 1

                    #Triangle duration counter
                    if self.playerObj.trianglePotionsCollected >= 1:
                        if tickCounter % 60 == 0:
                            self.triangleDurationText += 1
                            if self.triangleDurationText == 6:
                                self.triangleDurationText = 0
                                self.playerObj.trianglePotionsCollected = 0

                                #Unpause game background music
                                mixer.music.unpause()


                                        #Player touches obstacle
                    if self.obstacleObj.checkForObstacleCollisions():
                        #Triangle Form
                        if self.playerObj.trianglePotionsCollected >= 1:
                            #damagedAudio = mixer.Sound('C:\\Users\\USER\\Music\\tankhits.mp3')
                            self.load_Effects(".mp3")
                            self.playEffects("tankhits.mp3")
                            #damagedAudio.play()

                        #Regular form
                        else:
                            self.gameplayerCollided = True
                            self.playerObj.Hearts = self.playerObj.Hearts - 1

                            # damagedAudio = mixer.Sound('C:\\Users\\USER\\OneDrive\\Desktop\\PYTHON\\SuperEpicGames\\undertaleHurt.mp3')
                            # damagedAudio.play()
                            self.load_Effects("undertaleHurt.mp3")
                            self.playEffects("undertaleHurt.mp3")

                    #Player touches border:
                    if self.playerObj.checkForBorderCollision(ScreenWidth, ScreenHeight, keys):
                        self.playerCollidedWithBorder = True

                    #Reset values to default after losing
                    if self.playerObj.Hearts <= 0 and self.gameOver == False:
                        print("Player ran out of hearts")
                        self.playerObj.Hearts = 3
                        self.playerObj.trianglePotionsCollected = 0
                        self.finalScore = self.score
                        self.gameOver = True

                        #Log final score

                        # Log user's last score
                        self.saveLoadSystemObj.load_numbers_from_file()
                        self.saveLoadSystemObj.save_and_display_top5(self.finalScore)
                        self.saveLoadSystemObj.mainMenuLog()
                        self.score = 0

                        #Reset Hearts back to 3
                        #this stops the infinite loop

                    # draw the obstacles in obstacles[]
                    # break player if collided


                    # Yes, this is the correct parameters, due to the logic of (x,y)
                    screen.blit(printTime, (ScreenWidth - 795, ScreenHeight / 2 - 395))
                    screen.blit(printScore, (ScreenWidth - 350, ScreenHeight / 2 - 395))
                    screen.blit(printHearts, (ScreenWidth - 795, ScreenHeight /2 - 370))
                    screen.blit(printTriangle, (ScreenWidth - 795, ScreenHeight /2 - 300))

                if self.gameOver:
                    screen.fill(((0, 0, 0)))
                    pygame.mixer.music.pause()
                    self.obstacleObj.deleteAllObstacles()

                    #Transport player to the death map (unreachable area)
                    # self.playerObj.playerYCoord = 200
                    # self.playerObj.playerXCoord = 200

                    printLatestScore = font.render("You scored " + str(self.finalScore) + ", great job!", True,
                                                 (255, 255, 255))
                    screen.blit(printLatestScore, (ScreenWidth / 2 - 150, ScreenHeight / 2 - 50))


                    # Replay
                    if ScreenWidth / 2 - 150 <= userMouse[0] <= ScreenWidth / 2 + 30 and ScreenHeight / 2 + 50 <= \
                            userMouse[
                                1] <= ScreenHeight / 2 + 110:
                        pygame.draw.rect(screen, color_light,
                                         [ScreenWidth / 2 - 150, ScreenHeight / 2 + 50, 180, 60])

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.startClicking()
                            #Reset game variables back to default
                            self.score = 0
                            self.playerObj.Hearts = 3
                            self.gameOver = False
                            timeInSeconds = 0
                            pygame.mixer.music.unpause()

                            #Transport player back to default game location
                            self.playerObj.playerYCoord = 400
                            self.playerObj.playerXCoord = 400

                            gamePaused = False
                            self.potionObj.deleteAllPotions()
                            self.obstacleObj.deleteAllObstacles()
                    else:
                        pygame.draw.rect(screen, color_dark,
                                         [ScreenWidth / 2 - 150, ScreenHeight / 2 + 50, 180, 60])

                    exitText = font.render("Return", True,
                                           (255, 255, 255))
                    replayText = font.render("Try again ", True,
                                             (255, 255, 255))
                    yousuretext = font.render("You sure? :( ", True,
                                              (255,255,255))

                    screen.blit(replayText, (ScreenWidth / 2 - 150, ScreenHeight / 2 + 50))

                    # Exit
                    if ScreenWidth / 2 + 50 <= userMouse[0] <= ScreenWidth / 2 + 230 and ScreenHeight / 2 + 50 <= \
                            userMouse[
                                1] <= ScreenHeight / 2 + 110:
                        pygame.draw.rect(screen, color_light,
                                         [ScreenWidth / 2 + 50, ScreenHeight / 2 + 50, 180, 60])
                        screen.blit(yousuretext, (ScreenWidth / 2 + 50, ScreenHeight / 2 + 50))

                        # If event = mouseClick Do:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.mainMenu.returnedToMainMenu = True
                            self.startClicking()

                            if(self.mainMenu.returnedToMainMenu == True):
                                self.mainMenu.startMainMenu()
                                self.mainMenu.returnedToMainMenu = False

                    else:
                        pygame.draw.rect(screen, color_dark,
                                         [ScreenWidth / 2 + 50, ScreenHeight / 2 + 50, 180, 60])
                        screen.blit(exitText, (ScreenWidth / 2 + 50, ScreenHeight / 2 + 50))

                # DO NOT UPDATE MORE THAN ONCE!: This causes a flashy background effect from the black bg
                #You lose!
                #Display score, if score is highscore, print you got a new highscore
                #Add play again button

                pygame.display.update()

