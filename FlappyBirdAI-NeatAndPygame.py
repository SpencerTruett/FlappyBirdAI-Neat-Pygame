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