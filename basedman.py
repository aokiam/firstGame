import pygame
import sys
import random
import time
import re

from pygame.locals import *

WIDTH, HEIGHT = 1280, 720

BG_COLOR = (127, 138, 150)
MIKU = (7, 248, 187)
ADO = (75, 86, 107)
DAHYUN = (0, 0, 0)
WHITE = (255, 255, 255)

LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

pygame.init()

pygame.display.set_caption("BASEDman")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
kpop = ["twice", "g idle", "le sserafim", "itzy", "aespa", "illit", "newjeans", "loona", "stayc", "red velvet"]
vocaloid = ["miku", "rin", "len", "meiko", "kaito", "luka", "gumi", "neru", "teto", "mayu"]
jpop = ["ado", "tuyu", "vaundy", "takayan", "soraru", "mafumafu", "nqrse", "yorushika", "atarashii gakko", "eve"]

font = pygame.font.Font("Winkle-Regular.ttf", 40)
font_big = pygame.font.Font("Winkle-Regular.ttf", 50)

screen.fill(BG_COLOR)

def random(choice):
    rand_num = random.randint(0,len(kpop)-1)
    return rand_num

def words(number, choice):
    if choice == 1:
        artist = kpop[number]
    elif choice == 2:
        artist = vocaloid[number]
    elif choice == 3:
        artist = jpop[number]
    return artist

def startScreen():
    screen.blit(font_big.render("BASEDman", True, WHITE), (640, 30))
    screen.blit(font.render("hangman, but based!", True, WHITE), (640, 40))
    screen.blit(font.render("CATEGORIES", True, WHITE), (640, 70))
    screen.blit(font.render("Vocaloid", True, MIKU), (640, 40))
    screen.blit(font.render("J-Pop", True, ADO), (640, 40))
    screen.blit(font.render("K-Pop", True, DAHYUN), (640, 40))

def main():
    choice = 0

    startScreen()

    first = True