import game_framework
from pico2d import *
from ball import Ball
import sys
import random
import game_world

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 300
        self.frame = random.randint(0, 7)
        self.image = load_image('bird100x100x14.png')
        self.velocity = 500 # 속도 설정 

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity * game_framework.frame_time



        

    def draw(self):
       		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)	
        








