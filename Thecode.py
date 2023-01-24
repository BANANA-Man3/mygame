import time
import pygame
from random import randint
from sys import exit
hi = "hi"
#game start
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Awesome game")
#screen size
screen = pygame.display.set_mode((1275,700))

#sky
sky = pygame.Surface((1275,500))
sky.fill('Light Blue')
#town
road = pygame.Surface((1275,100))
road.fill('Brown')
road_rect = road.get_rect(topleft = (0,550))
grass = pygame.Surface((1275,50))
grass.fill('Green')
house = pygame.Surface((200,250))
house_rect = house.get_rect(topleft = (1025,300))
house.fill('Grey')
merchant = pygame.Surface((200,250))
merchant_rect = merchant.get_rect(topleft = (775,300))
merchant.fill('Grey')
petshop = pygame.Surface((200,250))
petshop_rect = petshop.get_rect(topleft = (525,300))
petshop.fill('Grey')
lab = pygame.Surface((200,250))
lab_rect = lab.get_rect(topleft = (275,300))
lab.fill('Grey')
quest = pygame.Surface((200,250))
quest_rect = quest.get_rect(topleft = (25,300))
quest.fill('Grey')
while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if house_rect.collidepoint(event.pos):
                print("house")
            if merchant_rect.collidepoint(event.pos):
                print("merchant")
            if petshop_rect.collidepoint(event.pos):
                print("petshop")
            if lab_rect.collidepoint(event.pos):
                print("lab")
            if quest_rect.collidepoint(event.pos):
                print("quest")
    screen.blit(sky,(0,0))
    screen.blit(road,road_rect)
    screen.blit(grass,(0,650))
    screen.blit(grass,(0,500))
    screen.blit(house,house_rect)
    screen.blit(merchant,merchant_rect)
    screen.blit(petshop,petshop_rect)
    screen.blit(lab,lab_rect)
    screen.blit(quest,quest_rect)
    
    pygame.display.update()
    clock.tick(60)