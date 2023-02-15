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
#sky
#sky = pygame.Surface((1275,500))
sky = pygame.image.load("town/skyimage.png").convert_alpha()
#town

road = pygame.image.load("town/roadimage.png").convert_alpha()
road_rect = road.get_rect(topleft = (0,550))

grass = pygame.Surface((1275,50))
grass.fill('Green')

#icons
mapicon = pygame.image.load("icons/mapiconimage.png").convert_alpha()
mapicon_rect = mapicon.get_rect(topleft = (1235,665))

#playerinventory
userinv = [{"itemset": "wood","itemtype": "Weapon","level":1,"rarity":"Legendary","damage":5},{"itemset": "wood","itemtype": "Weapon","level":1,"rarity":"Uncommon","damage":5}]#,{"itemset": "wood","itemtype": "Boots","level":1,"rarity":"Rare","damage":5},{"itemset": "wood","itemtype": "Leggings","level":1,"rarity":"Epic","damage":5},{"itemset": "wood","itemtype": "Chestplate","level":1,"rarity":"Legendary","damage":5},{"itemset": "wood","itemtype": "Helmet","level":1,"rarity":"Mythical","damage":5}]
equipeditems = [{"itemset": "wood","itemtype": "Weapon","level":1,"rarity":"Rare","damage":5},{"itemset": "wood","itemtype": "Helmet","level":1,"rarity":"Epic","damage":5}]#,{"itemset": "wood","itemtype": "Boots","level":1,"rarity":"Epic","damage":5},{"itemset": "wood","itemtype": "Leggings","level":1,"rarity":"Mythical","damage":5},{"itemset": "wood","itemtype": "Chestplate","level":1,"rarity":"Uncommon","damage":5},{"itemset": "wood","itemtype": "Helmet","level":1,"rarity":"Common","damage":5}]
surflist = []
rectlist = []
backlist = []
coins = 0
userlevel = 1
health = 100

def kill():
    global coins
    rancoins = random.randint(1,5)
    ranitem = random.randint(1,3)
    coins += rancoins
    getitem()
    if ranitem == 1:
        getitem()
def gethealth():
    global health
    newhealth = 100
    for i in equipeditems:
        if i["itemtype"] == "Weapon":
            continue
        else:
            newhealth += i["damage"]
    health = newhealth
def getitem():
    global userlevel
    irareity = random.randint(1,10000)
    itype = random.randint(0,4)
    typelist = ["Helmet","Chestplate","Leggings","Boots","Weapon"]
    newtype = typelist[itype]
    raritylist = ["Common","Uncommon","Rare","Epic","Legendary","Mythical"]
    if userlevel == 1:
        newd = random.randint(2,7)
    if irareity <= 5000:#50
        newrareity = "Common"
    elif irareity <= 7500:#20
        newrareity = "Uncommon"
        newd += 1
    elif irareity <= 9500:#12.5
        newrareity = "Rare"
        newd += 2
    elif irareity <= 9900:#11.5
        newrareity = "Epic"
        newd += 3
    elif irareity <= 9999:#.99
        newrareity = "Legendary"
        newd += 4
    elif irareity == 10000:#.01
        newrareity = "Mythical"
        newd += 5
    userinv.append({"itemset":"wood","itemtype":newtype,"level":1,"rarity": newrareity,"damage":newd})
def getdamage():
    count = 0
    for i in equipeditems:
        if i["itemtype"] == "Weapon":
            return equipeditems[count]["damage"]
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
                mobh1 -= getdamage()
                attackcounter = 0
                if mobh1 <= 0 and m1alive:
                    m1alive = False
                    kill()
            if selectedmob == "mob2num":
                mobh2 -= getdamage()
                attackcounter = 0
                if mobh2 <= 0 and m2alive:
                    m2alive = False
                    kill()
            if selectedmob == "mob3num":
                mobh3 -= getdamage()
                attackcounter = 0
                if mobh1 <= 0 and m3alive:
                    m3alive = False
                    kill()
        if not m1alive and not m2alive and not m3alive:
            won()
            inside = False
        insidemap = pygame.image.load("map_scene/fightscene.png").convert_alpha()
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
    print("you WIn!")

def getequiped(n,e):
    c = 0
    itype = n["itemtype"]
    
    for i in equipeditems:
        if i["itemtype"] == itype:
            userinv.append(i)
            equipeditems.pop(c)
            
        c += 1
    equipeditems.append(n)
    userinv.pop(e)
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
                    inside = False
        insidemap = pygame.image.load("map_scene/map.png").convert_alpha()
        regularfight = pygame.image.load("map_scene/regularfighticon.png").convert_alpha()
        regularfight_rect = regularfight.get_rect(topleft = (535,365))
        screen.blit(insidemap,(0,0))
        screen.blit(arrow,arrow_rect)
        screen.blit(regularfight,regularfight_rect)
        pygame.display.update()
        clock.tick(60)
def get_color(slot):
    if userinv[slot]["rarity"] == "Common":
         return "backgroundcolors/Common_Background.png"
    if userinv[slot]["rarity"] == "Uncommon":
         return "backgroundcolors/Uncommon_Background.png"
    if userinv[slot]["rarity"] == "Rare":
         return "backgroundcolors/Rare_Background.png"
    if userinv[slot]["rarity"] == "Epic":
         return "backgroundcolors/Epic_Background.png"
    if userinv[slot]["rarity"] == "Legendary":
         return "backgroundcolors/Legendary_Background.png"
    if userinv[slot]["rarity"] == "Mythical":
         return "backgroundcolors/Mythic_Background.png"
#find what pic to diplay
def get_display(slot):
    if userinv[slot]["itemtype"] == "Weapon":
        return "weapons/testweapon.png"
    if userinv[slot]["itemtype"] == "Helmet":
        return "helmets/testhelmet.png"
    if userinv[slot]["itemtype"] == "Chestplate":
        return "chestplates/testchestplate.png"
    if userinv[slot]["itemtype"] == "Leggings":
        return "leggings/testleggings.png"
    if userinv[slot]["itemtype"] == "Boots":
        return "boots/testboots.png" 
def get_equiped_display(slot):
    if equipeditems[slot]["itemtype"] == "Weapon":
        return "weapons/testweapon.png"
    if equipeditems[slot]["itemtype"] == "Helmet":
        return "helmets/testhelmet.png"
    if equipeditems[slot]["itemtype"] == "Chestplate":
        return "chestplates/testchestplate.png"
    if equipeditems[slot]["itemtype"] == "Leggings":
        return "leggings/testleggings.png"
    if equipeditems[slot]["itemtype"] == "Boots":
        return "boots/testboots.png" 

def getdict():
    global surflist
    global rectlist
    global backlist
    backlist = []
    surflist = []
    rectlist = [] 
    count = len(userinv)
    y = 280
    x = 272
    nextline = 0
    for i in range(count):
        surflist.append(pygame.image.load(get_display(i)).convert_alpha())
        rectlist.append(surflist[i].get_rect(topleft = (x,y)))
        backlist.append(pygame.image.load(get_color(i)).convert_alpha())
        x += 62
        nextline += 1
        if nextline == 7:
            x = 272
            y += 62
            nextline = 0
    count = len(userinv)
    for i in range(count):
        screen.blit(backlist[i],rectlist[i])
        screen.blit(surflist[i],rectlist[i])
def equiped_color(slot):
    if equipeditems[slot]["rarity"] == "Common":
         return "backgroundcolors/Common_Background.png"
    if equipeditems[slot]["rarity"] == "Uncommon":
         return "backgroundcolors/Uncommon_Background.png"
    if equipeditems[slot]["rarity"] == "Rare":
         return "backgroundcolors/Rare_Background.png"
    if equipeditems[slot]["rarity"] == "Epic":
         return "backgroundcolors/Epic_Background.png"
    if equipeditems[slot]["rarity"] == "Legendary":
         return "backgroundcolors/Legendary_Background.png"
    if equipeditems[slot]["rarity"] == "Mythical":
         return "backgroundcolors/Mythic_Background.png"
def display_equiped():
    count = 0
    for i in equipeditems:
        y = 275
        if i["itemtype"] == "Helmet":
            helmet_surf = pygame.image.load(get_equiped_display(count)).convert_alpha()
            helmet_rect = helmet_surf.get_rect(topleft = (1004,y))
            helmet_csurf = pygame.image.load(equiped_color(count)).convert_alpha()
            screen.blit(helmet_csurf,helmet_rect)
            screen.blit(helmet_surf,helmet_rect)
        y += 104
        if i["itemtype"] == "Chestplate":
            chestplate_surf = pygame.image.load(get_equiped_display(count)).convert_alpha()
            chestplate_rect = chestplate_surf.get_rect(topleft = (1004,y))
            chestplate_csurf = pygame.image.load(equiped_color(count)).convert_alpha()
            screen.blit(chestplate_csurf,chestplate_rect)
            screen.blit(chestplate_surf,chestplate_rect)
        y += 104
        if i["itemtype"] == "Leggings":
            leggings_surf = pygame.image.load(get_equiped_display(count)).convert_alpha()
            leggings_rect = leggings_surf.get_rect(topleft = (1004,y))
            leggings_csurf = pygame.image.load(equiped_color(count)).convert_alpha()
            screen.blit(leggings_csurf,leggings_rect)
            screen.blit(leggings_surf,leggings_rect)
        y += 104
        if i["itemtype"] == "Boots":
            boots_surf = pygame.image.load(get_equiped_display(count)).convert_alpha()
            boots_rect = boots_surf.get_rect(topleft = (1004,y))
            boots_csurf = pygame.image.load(equiped_color(count)).convert_alpha()
            screen.blit(boots_csurf,boots_rect)
            screen.blit(boots_surf,boots_rect)
        if i["itemtype"] == "Weapon":
            weapon_surf = pygame.image.load(get_equiped_display(count)).convert_alpha()
            weapon_rect = weapon_surf.get_rect(topleft = (1120,430))
            weapon_csurf = pygame.image.load(equiped_color(count)).convert_alpha()
            screen.blit(weapon_csurf,weapon_rect)
            screen.blit(weapon_surf,weapon_rect)
        count += 1
def ininventory():
    global arrow
    global arrow_rect
    global coins
    inside = True
    while inside:
        gethealth()
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    inside = False
                for index in range(len(userinv)):
                    if rectlist[index].collidepoint(mouse_pos):
                        getequiped(userinv[index],index) 
        insideinventory = pygame.image.load("inventory.png").convert_alpha()
        coins_surf = test_font.render("coins: "+str(coins),False,(64,64,64))
        screen.blit(insideinventory,(0,0))
        screen.blit(arrow,arrow_rect)
        screen.blit(coins_surf,(20,60))
        y = 278
        x = 270
        for i in range(7):
            pygame.draw.line(screen,(64,64,64),(270,y),(705,y),2)
            y += 62
        for i in range(8):
            pygame.draw.line(screen,(64,64,64),(x,278),(x,649),2)
            x += 62
        y = 275
        for i in range(4):
            pygame.draw.rect(screen, (64,64,64), [1004,y,60,60],  2)
            y += 104
        y = 280
        pygame.draw.rect(screen, (64,64,64), [1120,430,60,60],  2)
        pygame.draw.rect(screen, (64,64,64), [890,430,60,60],  2)
        display_equiped()
        getdict()
        w = 200
        l = 200
        for index in range(len(userinv)):
            if rectlist[index].collidepoint(mouse_pos):
                count = 1
                for i in mouse_pos:
                    if count == 1:
                        x = i
                        count += 1
                    else:
                        y = i
                x -= 220
                pygame.draw.rect(screen, (64,64,64), [x,y,w,l])
                damage = userinv[index]["damage"]
                damage_surf = test_font.render("damage: "+str(damage),False,(104,255,64))
                x += 10
                y += 10
                screen.blit(damage_surf,(x,y))  
        pygame.display.update()
        clock.tick(60)
inventoryicon = pygame.image.load("icons/inventoryiconimage.png").convert_alpha()
inventoryicon_rect = inventoryicon.get_rect(topleft = (1205,665))
#arrows
arrow = pygame.image.load("icons/arrowimage.png").convert_alpha()
arrow_rect = arrow.get_rect(topleft = (20,630))
#buildings
house = pygame.image.load("town/houseimage.png").convert_alpha()
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
        insidehouse = pygame.image.load("town/insidehouseimage.png").convert_alpha()
        screen.blit(insidehouse,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
merchant = pygame.image.load("town/merchantimage.png").convert_alpha()
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
        insidemerchant = pygame.image.load("town/insidemerchantimage.png").convert_alpha()
        screen.blit(insidemerchant,(0,0))
        screen.blit(arrow,arrow_rect)
        
        pygame.display.update()
        clock.tick(60)
petshop = pygame.image.load("town/petshopimage.png").convert_alpha()
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
        petshopimage = pygame.image.load("town/insidepetshop.png").convert_alpha()
        screen.blit(petshopimage,(0,0))
        screen.blit(arrow,arrow_rect)
        getdict()
        pygame.display.update()
        clock.tick(60)
lab = pygame.image.load("town/skilltreeimage.png").convert_alpha()
lab_rect = lab.get_rect(topleft = (275,300))

quest = pygame.image.load("town/questsimage.png").convert_alpha()
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