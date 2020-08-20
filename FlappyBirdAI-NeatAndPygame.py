import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird:
  IMGS = BIRD_IMGS #Bird Images
  MAX_ROTATION = 25 #Max Rotation up or down
  ROT_VEL = 20 #How much rotation on each fram
  ANIMATION_TIME = 5 #How fast or slow the wings flap in the frame

  def __init__(self, x, y):
    self.x = x #Starting Position
    self.y = y #Starting Position
    self.tilt = 0 #Initial Tilt angle
    self.tick_count = 0 #Used for physics
    self.vel = 0 #Not moving initially
    self.height = self.y #For move and tilt
    self.img_count = 0 #Which image we are currently showing
    self.img = self.IMGS[0] #Starting with initial image
    
    def jump(self):
      self.vel = -10.5 #Top left is 0,0; so up is negative
      self.tick_count = 0 #Resets for when we are changing direction of velocity
      self.height = self.y #Where the bird jumped from
          
    def move(self):
      self.tick_count += 1 #Add to tick count "since last jump"
      d = self.vel*self.tick_count + 1.5*self.tick_count**2 #Based on current velocity, how much we're moving up or down; Creates the arc during a jump

      if d >= 16: #Terminal Velocity wont be higher than 16
        d = 16
      
      if d < 0: #Fine tunes the jump a bit
        d -= 2

      self.y = self.y + d #Adds the calculated value above to current y position

      if d < 0 or self.y < self.height + 50: #Creates upward tilt at the upward arc of jump
        if self.tilt < self.MAX_ROTATION:
          self.tilt = self.MAX_ROTATION
      else:
        if self.tilt > -90:
          self.tilt -= self.ROT_VEL