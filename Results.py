import pygame 
import sys
from src import locations
from src import resutls
from src import display

class results: 

  def gameLoop(self):
    while self.state == "GAME":
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()
          if event.type == pygame.K_D:
            self.type == self.dunkin
          if(event.key == pygame.K_C):
            self.type == self.c4()
          elif(event.key == pygame.K_L):
            self.type == self.library()
          elif(event.key == pygame.K_U):
            self.type == self.undergrounds()
          elif(event.key == pygame.K_G):
            self.type == self.gym()
          elif(event.key == pygame.K_T):
            self.type == self.track()
          elif(event.key == pygame.K_N):
            self.type == self.naturepres()
          elif(event.key == pygame.K_LT):
            self.type == self.laketaco()
          elif(event.key == pygame.K_A):
            self.type == self.academicA()
          elif(event.key == pygame.K_J):
            self.type == self.jazzmans()
          elif(event.key == pygame.K_S):
            self.type == self.starbucks()
          elif(event.key == pygame.K_E):
            self.type == self.eventcenter()
          elif(event.key == pygame.K_H):
            self.type == self.hinman()
