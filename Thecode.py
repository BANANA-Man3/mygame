import time
import pygame
from random import randint
from sys import exit
hi = "hi"
#game start
pygame.init()
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
pygame.display.set_caption("Awesome game")
#screen size
screen = pygame.display.set_mode((1275,700))

#sky
#sky = pygame.Surface((1275,500))
sky = pygame.image.load("skyimage.png").convert_alpha()
#town
road = pygame.image.load("roadimage.png").convert_alpha()
road_rect = road.get_rect(topleft = (0,550))

grass = pygame.Surface((1275,50))
grass.fill('Green')
#icons
mapicon = pygame.image.load("mapiconimage.png").convert_alpha()
mapicon_rect = mapicon.get_rect(topleft = (1235,665))
def inmap():
    global arrow
    global arrow_rect
    inside = True
    while inside:

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    inside = False
        insidemap = pygame.image.load("map.png").convert_alpha()
        screen.blit(insidemap,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
def ininventory():
    global arrow
    global arrow_rect
    inside = True
    while inside:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    inside = False
        insideinventory = pygame.image.load("inventory.png").convert_alpha()
        screen.blit(insideinventory,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
inventoryicon = pygame.image.load("inventoryiconimage.png").convert_alpha()
inventoryicon_rect = inventoryicon.get_rect(topleft = (1205,665))
#arrows
arrow = pygame.image.load("arrowimage.png").convert_alpha()
arrow_rect = arrow.get_rect(topleft = (20,630))
#buildings
house = pygame.image.load("houseimage.png").convert_alpha()
house_rect = house.get_rect(topleft = (1025,300))


def inhome():
    global arrow
    global arrow_rect
    inside = True
    while inside:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    inside = False
        insidehouse = pygame.image.load("insidehouseimage.png").convert_alpha()
        screen.blit(insidehouse,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
merchant = pygame.image.load("merchantimage.png").convert_alpha()
merchant_rect = merchant.get_rect(topleft = (775,300))
def inmerchantfunc():
    global arrow
    global arrow_rect
    inside = True
    while inside:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    inside = False
        insidemerchant = pygame.image.load("insidemerchantimage.png").convert_alpha()
        screen.blit(insidemerchant,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
petshop = pygame.image.load("petshopimage.png").convert_alpha()
petshop_rect = petshop.get_rect(topleft = (525,300))
def inpetshopfunc():
    global arrow
    global arrow_rect
    inside = True
    while inside:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    inside = False
        petshopimage = pygame.image.load("insidepetshop.png").convert_alpha()
        screen.blit(petshopimage,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
lab = pygame.image.load("skilltreeimage.png").convert_alpha()
lab_rect = lab.get_rect(topleft = (275,300))

quest = pygame.image.load("questsimage.png").convert_alpha()
quest_rect = quest.get_rect(topleft = (25,300))

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if house_rect.collidepoint(event.pos):
                print("house")
                inhome()
            if merchant_rect.collidepoint(event.pos):
                print("merchant")
                inmerchantfunc()
            if petshop_rect.collidepoint(event.pos):
                print("petshop")
                inpetshopfunc()
            if lab_rect.collidepoint(event.pos):
                print("lab")
            if quest_rect.collidepoint(event.pos):
                print("quest")
            if inventoryicon_rect.collidepoint(event.pos):
                print("inventory")
                ininventory()
            if mapicon_rect.collidepoint(event.pos):
                print("MAp")
                inmap()
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_m:
                inmap()
            if event.key == pygame.K_i:
                ininventory()

#     print(hi)
    screen.blit(sky,(0,0))
    screen.blit(road,road_rect)
    screen.blit(grass,(0,650))
    screen.blit(grass,(0,500))
    screen.blit(house,house_rect)
    screen.blit(merchant,merchant_rect)
    screen.blit(petshop,petshop_rect)
    screen.blit(lab,lab_rect)
    screen.blit(quest,quest_rect)
    screen.blit(mapicon,mapicon_rect)
    screen.blit(inventoryicon,inventoryicon_rect)
    
    pygame.display.update()
    clock.tick(60)