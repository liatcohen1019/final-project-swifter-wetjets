import pygame
import sys
from src import negcovid
from src import poscovid

class user: 
  def __init__(self, width=640, height=480):
    pygame.init()
    self.width = 500
    self.height = 300
    self.blue = (0,0,255)
    self.red = (255,0,0)
    self.green = (0,255,0)
    self.screen = pygame.display.set_mode((self.width,self.height))
    self.screen.fill(self.blue)
    self.font = pygame.font.SysFont(None, 32)
    pygame.display.flip()
    self.state = "DORM"
    self.negative = negcovid.Negcovid("Negative", 50, 80, "assets/negcovid.png")
    self.neg_sprites = pygame.sprite.Group((self.negative,))
    self.positive = poscovid.Poscovid("Positive", 50, 80, "assets/poscovid.png")
    self.pos_sprites = pygame.sprite.Group((self.positive,))
  

  def showtext(self, x, y, textdisplay):
    start = self.font.render(textdisplay, True, (0,0,0))
    self.screen.blit(start, (x, y))
    
  def mainLoop(self):
    while True:
        if(self.state == "DORM"):
            self.gameDormLoop()
        elif(self.state == "DUNKIN"):
            self.gameDunkinLoop()
        elif(self.state == "LIBRARY"):
            self.gameLibraryLoop()
        elif(self.state == "UNDERGROUNDS"):
            self.gameUndergroundsLoop()
        elif(self.state == "ACADEMICA"):
            self.gameAcademicALoop()
        elif(self.state == "LAKETACO"):
            self.gameLaketacoLoop()
        elif(self.state == "LECTURE"):
            self.gameLectureLoop()
        elif(self.state == "NATURE"):
            self.gameNatureLoop()
        elif(self.state == "C4"):
            self.gameC4Loop()
        elif(self.state == "TRACK"):
            self.gameTrackLoop()
        elif(self.state == "GYM"):
            self.gameGymLoop()
        elif(self.state == "JAZZMANS"):
            self.gameJazzmansLoop()
        elif(self.state == "STARBUCKS"):
            self.gameStarbucksLoop()
        elif(self.state == "EVENTS"):
            self.gameEventsLoop()
        elif(self.state == "HINMAN"):
            self.gameHinmanLoop()
    
  def gameDormLoop(self):
    self.showtext(50, 50, 'You are in your dorm!')
    self.showtext(50, 200,'Press the d key to go to Dunkin Donuts')
    self.showtext(50, 250,'Press the c key to go to C4 dining hall')
    pygame.display.flip()
    while self.state == "DORM":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_d):
                    self.state = "DUNKIN"
                elif(event.key == pygame.K_c):
                    self.state = "C4"
        pygame.display.flip()
      
    
  def gameC4Loop(self):
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.green)
    self.showtext(50, 50, 'You did not get COVID!')
    self.neg_sprites.draw(self.screen)
    pygame.display.flip()
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(50, 50, 'You are in C4 dining hall!')
    self.showtext(50, 200,'Press the g key to go to the gym')
    self.showtext(50, 250,'Press the t key to go to the track')
    pygame.display.flip()
    while self.state == "C4":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_g):
                    self.state = "GYM"
                elif(event.key == pygame.K_t):
                    self.state = "TRACK"
        pygame.display.flip()  


  def gameDunkinLoop(self):
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.green)
    self.showtext(50, 50, 'You did not get COVID!')
    self.neg_sprites.draw(self.screen)
    pygame.display.flip()
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(50, 50, 'You are in dunkin!')
    self.showtext(50, 200,'Press the l key to go to the library')
    self.showtext(50, 250,'Press the u key to go to the undergrounds')
    pygame.display.flip()
    while self.state == "DUNKIN":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_l):
                    self.state = "LIBRARY"
                elif(event.key == pygame.K_u):
                    self.state = "UNDERGROUNDS"
        pygame.display.flip() 

  def gameLibraryLoop(self):
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.green)
    self.showtext(50, 50, 'You did not get COVID!')
    self.neg_sprites.draw(self.screen)
    pygame.display.flip()
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(50, 50, 'You are in the Library!')
    self.showtext(50, 200,'Press the a key to go to Academic A building')
    self.showtext(50, 250,'Press the o key to go to laketaco')
    pygame.display.flip()
    while self.state == "LIBRARY":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_o):
                    self.state = "LAKETACO"
                elif(event.key == pygame.K_a):
                    self.state = "ACADEMICA"
        pygame.display.flip()  

  def gameUndergroundsLoop(self):
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.green)
    self.showtext(50, 50, 'You did not get COVID!')
    self.neg_sprites.draw(self.screen)
    pygame.display.flip()
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(50, 50, 'You are in the Undergrounds!')
    self.showtext(50, 200,'Press the h key to go to the lecture hall')
    self.showtext(50, 250,'Press the n key to go to the nature preserve')
    pygame.display.flip()
    while self.state == "UNDERGROUNDS":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_h):
                    self.state = "lECTURE"
                elif(event.key == pygame.K_n):
                    self.state = "NATURE"
        pygame.display.flip()  

  def gameGymLoop(self):
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.red)
    self.showtext(50, 50, 'You got COVID! :(')
    self.pos_sprites.draw(self.screen)
    pygame.display.flip()
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(100, 100, 'Game over')
    pygame.display.flip()
    pygame.time.wait(3000)
    sys.exit()
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(50, 50, 'You are in the gym!')
    self.showtext(50, 200,'Press the j key to go to the Jazzmans')
    self.showtext(50, 250,'Press the s key to go to the Starbucks')
    pygame.display.flip()
    while self.state == "GYM":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_j):
                    self.state = "JAZZMANS"
                elif(event.key == pygame.K_s):
                    self.state = "STARBUCKS"
        pygame.display.flip()  

  def gameTrackLoop(self):
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.green)
    self.showtext(50, 50, 'You did not get COVID!')
    self.neg_sprites.draw(self.screen)
    pygame.display.flip()
    pygame.time.wait(3000)
    self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
    self.screen.fill(self.blue)
    self.showtext(50, 50, 'You are at the track!')
    self.showtext(50, 200,'Press the e key to go to the eventscenter')
    self.showtext(50, 250,'Press the h key to go to the Hinman')
    pygame.display.flip()
    while self.state == "TRACK":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_e):
                    self.state = "EVENTS"
                elif(event.key == pygame.K_h):
                    self.state = "HINMAN"
        pygame.display.flip()  

  def gameHinmanLoop(self):
    while self.state == "HINMAN":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_h):
              self.state = "red"
      self.screen.fill(self.red)
      self.showtext(50, 50, 'You got COVID!')
      self.pos_sprites.draw(self.screen)
      pygame.display.flip()  
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'Game over')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit()

  def gameEventsLoop(self):
    while self.state == "EVENTS":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_e):
              self.state = "green"
      self.screen.fill(self.green)
      self.showtext(50, 50, 'You did not get COVID!')
      self.neg_sprites.draw(self.screen)
      pygame.display.flip()
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'You Win!!')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit()

  def gameStarbucksLoop(self):
    while self.state == "STARBUCKS":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_s):
              self.state = "red"
      self.screen.fill(self.red)
      self.showtext(50, 50, 'You got COVID!')
      self.pos_sprites.draw(self.screen)
      pygame.display.flip()
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'Game over')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit()

  def gameJazzmansLoop(self):
    while self.state == "JAZZMANS":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_j):
              self.state = "green"
      self.screen.fill(self.green)
      self.showtext(50, 50, 'You did not get COVID!')
      self.neg_sprites.draw(self.screen)
      pygame.display.flip()
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'You Win!!')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit()

  def gameNatureLoop(self):
    while self.state == "NATURE":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_n):
              self.state = "green"
      self.screen.fill(self.green)
      self.showtext(50, 50, 'You did not get COVID!')
      self.neg_sprites.draw(self.screen)
      pygame.display.flip() 
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'You Win!!')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit()
      
  def gameLectureLoop(self):
    while self.state == "LECTURE":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_l):
              self.state = "red"
      self.screen.fill(self.red)
      self.showtext(50, 50, 'You got COVID!')
      self.pos_sprites.draw(self.screen)
      pygame.display.flip()
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'Game over')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit() 

  def gameLaketacoLoop(self):
    while self.state == "LAKETACO":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_o):
              self.state = "green"
      self.screen.fill(self.green)
      self.showtext(50, 50, 'You did not get COVID!')
      self.neg_sprites.draw(self.screen)
      pygame.display.flip() 
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'You Win!!')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit()
      
  def gameAcademicALoop(self):
    while self.state == "ACADEMICA":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_a):
              self.state = "red"
      self.screen.fill(self.red)
      self.showtext(50, 50, 'You got COVID!')
      self.pos_sprites.draw(self.screen)
      pygame.display.flip()
      pygame.time.wait(3000)
      self.screen.fill(pygame.Color("black"), (0, 0, 500, 300))
      self.screen.fill(self.blue)
      self.showtext(100, 100, 'Game over')
      pygame.display.flip()
      pygame.time.wait(3000)
      sys.exit() 
    