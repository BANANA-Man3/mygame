import time
import pygame
from random import randint
from sys import exit
#game start
pygame.init()
clock = pygame.time.Clock()
#screen size
screen = pygame.display.set_mode((1275,700))

#sky
sky = pygame.Surface((1275,500))
sky.fill('Light Blue')
#town
road = pygame.Surface((1275,100))
road.fill('Brown')
#roadrect = road.get_rect(lopleft =)
grass = pygame.Surface((1275,50))
grass.fill('Green')
house = pygame.Surface((200,250))
house.fill('Grey')
merchant = pygame.Surface((200,250))
merchant.fill('Grey')
petshop = pygame.Surface((200,250))
petshop.fill('Grey')
lab = pygame.Surface((200,250))
lab.fill('Grey')
quest = pygame.Surface((200,250))
quest.fill('Grey')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky,(0,0))
    screen.blit(road,(0,550))
    screen.blit(grass,(0,650))
    screen.blit(grass,(0,500))
    screen.blit(house,(1025,300))
    screen.blit(merchant,(775,300))
    screen.blit(petshop,(525,300))
    screen.blit(lab,(275,300))
    screen.blit(quest,(25,300))
    pygame.display.update()
    clock.tick(60)