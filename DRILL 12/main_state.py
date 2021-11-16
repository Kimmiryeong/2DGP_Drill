import random
import json
import os

from pico2d import *
import game_framework
import game_world
from bird import Bird
from boy import Boy
from grass import Grass
from ball import Ball

name = "MainState"

boy = None
grass = None
birds =  None
balls = []
big_balls = []


def collide(a, b):
    # fill here
    return True




def enter():
    global boy, birds
    boy = Boy()
    birds = [Bird() for i in range(5)]
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for Birds in birds:
        Birds.update()
       

    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    for Birds in birds:
        Birds.draw()
    update_canvas()






