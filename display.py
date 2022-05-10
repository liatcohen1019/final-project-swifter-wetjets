import pygame
import sys
import random

  

pygame.init()
width = 800
height = 600
red = [255,0,0]
screen = pygame.display.set_mode([500,500])
background = pygame.Surface(screen.get_size()).convert()

background.fill(red)
pygame.display.flip()

def mainLoop(self):
      while True:
          if(self.state == "GAME"):
              self.gameLoop()
          elif(self.state == "GAMEOVER"):
              self.gameOver()

def gameLoop():
  something
def gameOver():
  something
  
background.fill((250,250,250))

running = True 
while running: 
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:  
        running = False
    elif event.type == pygame.QUIT:
      running == False 

  pygame.display.flip()
pygame.quit()
  
  
