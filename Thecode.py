import time
import pygame
import random
from sys import exit
hi = "hi"
#game start
pygame.init()
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
pygame.font.init()
pygame.display.set_caption("Awesome game")
#screen size
screen = pygame.display.set_mode((1275,700))
#playerinventory 
userinv = [{"equiped":True,"itemset": "wood","type": "Weapon","level":1,"rarity":"Common","damage":5}]
coins = 0
health = 100
def kill():
    global coins
    rancoins = random.randint(1,5)
    ranitem = random.randint(1,3)
    coins += rancoins
    getitem()
    if ranitem == 1:
        getitem()

def getitem():
    irareity = random.randint(1,10000)
    itype = random.randint(0,4)
    typelist = ["Helmet","Chestplate","Leggings","Boots","Weapon"]
    newtype = typelist[itype]
    raritylist = ["Common","Uncommon","Rare","Epic","Legendary","Mythical"]
    if irareity <= 5000:#50
        newrareity = "Common"
    elif irareity <= 7500:#20
        newrareity = "Uncommon"
    elif irareity <= 9500:#12.5
        newrareity = "Rare"
    elif irareity <= 9900:#11.5
        newrareity = "Epic"
    elif irareity <= 9999:#.99
        newrareity = "Legendary"
    elif irareity == 10000:#.01
        newrareity = "Mythical"
    userinv.append({"equiped":False,"type":newtype,"level":1,"rarity": newrareity,"damage":1})
    print(userinv)
def getdamage():
    count = 0
    for i in userinv:
        if i["equiped"] == True:
            return userinv[count]["damage"]
        count += 1
damage = getdamage()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
#fight
def fight(mobn1,mobn2,mobn3,mobd1,mobd2,mobd3,mobh1,mobh2,mobh3):
    inside = True
    mobn1surf = test_font.render(mobn1,False,(64,64,64))
    mobn2surf = test_font.render(mobn2,False,(64,64,64))
    mobn3surf = test_font.render(mobn3,False,(64,64,64))
    mob1 = pygame.image.load("monsters/testmonster.png").convert_alpha()
    mob2 = pygame.image.load("monsters/testmonster.png").convert_alpha()
    mob3 = pygame.image.load("monsters/testmonster.png").convert_alpha()
    mob1_rect = mob1.get_rect(topleft = (635,265))
    mob2_rect = mob2.get_rect(topleft = (235,265))
    mob3_rect = mob3.get_rect(topleft = (1035,265))
    selectedmob = "mob1num"
    attackcounter = 0
    m1alive = True
    m2alive = True
    m3alive = True
    while inside:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mob1_rect.collidepoint(event.pos):
                    selectedmob = "mob1num"
                if mob2_rect.collidepoint(event.pos):
                    selectedmob = "mob2num"
                if mob3_rect.collidepoint(event.pos):
                    selectedmob = "mob3num"
        attackcounter += 1
        if attackcounter >= 60:
            if selectedmob == "mob1num":
                print(getdamage())
                mobh1 -= getdamage()
                attackcounter = 0
                if mobh1 <= 0:
                    m1alive = False
                    kill()
            if selectedmob == "mob2num":
                mobh2 -= getdamage()
                print(mobh2)
                attackcounter = 0
                if mobh2 <= 0:
                    m2alive = False
                    kill()
            if selectedmob == "mob3num":
                mobh3 -= getdamage()
                print(mobh3)
                attackcounter = 0
                if mobh1 <= 0:
                    m3alive = False
                    kill()
        if not m1alive and not m2alive and not m3alive:
            won()
            inside = False
        insidemap = pygame.image.load("fightseen.png").convert_alpha()
        screen.blit(insidemap,(0,0))
        screen.blit(mobn1surf,(700,200))
        screen.blit(mobn2surf,(400,200))
        screen.blit(mobn3surf,(1000,200))
        if mobh1 >= 0:
            screen.blit(mob1,mob1_rect)
        if mobh2 >= 0:
            screen.blit(mob2,mob2_rect)
        if mobh3 >= 0:
            screen.blit(mob3,mob3_rect)
        pygame.display.update()
        clock.tick(60)
def won():
    ""
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
                if regularfight_rect.collidepoint(event.pos):
                    fight("joe biden","jeffery bezos","bill clinton",1,1,1,5,5,5)
        insidemap = pygame.image.load("map.png").convert_alpha()
        regularfight = pygame.image.load("regularfighticon.png").convert_alpha()
        regularfight_rect = regularfight.get_rect(topleft = (535,365))
        screen.blit(insidemap,(0,0))
        screen.blit(arrow,arrow_rect)
        screen.blit(regularfight,regularfight_rect)
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