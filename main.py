# *********************************************************
# Program: DodgeCube.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL7L
# Year: 2023/24 Trimester 1
# Names: Timothy Kew Wen Tzun | Kim Hong Zhang | AVINAESH KUMAR A/L KULASEGARAN | Teo Kok Tai
# IDs: Tim: 1221108448  | Kim: 1221106260 | Avi : 1221108241 | Teo: 1221104917
# Emails: 1221108448@student.MMU.my | 1221106260@student.MMU.my | 1221108241@student.mmu.edu.my | 1221104917@student.mmu.edu.my
# Phones: +60 11-5911-1237 | +60 12-575 1521 | +60 10-552 8654 | +60 11-3658 5457
# *********************************************************

import pygame

from Game import Game
from MainMenu import MainMenu

mainmenu1 = MainMenu()
mainmenu1.startMainMenu()

"""
Last updated: 24/12/2023

SOURCES:

This game has been assisted from various sources listed down below:
1) Stack overflow
2) Geeks for Geeks
   -https://www.geeksforgeeks.org/python-display-images-with-pygame/
   
3) https://pygame.readthedocs.io/en/latest/index.html (Pygame read the docs)
4) https://www.knowledgehut.com/tutorials/python-tutorial/python-file-io
5) https://docs.python.org/

The logic is created by we the humans while the bugs and syntax error are corrected by chatGPT(some!)


--Update logs--
1) Exit button has been replaced to return (FOR GAME OVER SCREEN)
   -Now allows user to return to the main menu without executing the code twice
   
2) Optimized the game over screen(Now only accepts one pygame event)

3) Added clicking noises to buttons
   -Clicking sound just for fun
   
4) Improved user friendliness of program
   -Introduced automatic file audio directory detection
   -No longer requires user to hardcode the audio directory into their system
   
5) Optimized again
   -All current obstacles will be decimated after game over screen is triggered
   -Score is resetted to zero after game over and after score logging
   
   Hopefully this will stop the game freezing after game over screen

6) New leaderboard system
   -The top 5 scores logged by the system will be displayed in the leaderboard screen which can be accessed through the main menu
   -saved_numbers5.json MUST CONTAIN an array filled with 5 elements or else it will cause a fatal error
   
   
--Bugs--
1) Game will freeze if user exceeds 2000 after losing (FIXED)
   -Error caused by obstacles not being deleted after game ends
   
2) Extremely laggy game-over screen (FIXED)
   -Error caused by calling too many pygame event loops to handle click detection

"""
