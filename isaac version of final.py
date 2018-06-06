#Additional feature
import pygame
from pygame.locals import *

def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    global name
    name = ""
    newfont = pygame.font.SysFont("Calibri", 35, bold = True)
    font = pygame.font.Font(None, 50)
    prompt = newfont.render("Enter username below", 1, (200,50,55))
    tip = newfont.render("Press ENTER when done", 1, (200,50,55))
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    return name
            elif evt.type == QUIT:
                return
        screen.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        screen.blit(prompt, (60, 80))
        screen.blit(tip, (60, 200))
        pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()


import pygame, sys, pygame.mixer, pygame as pg
import pygbutton
import random
import csv
import time
from collections import defaultdict
from pygame.locals import *

#initalise pygame
pygame.init()

#Globally Initalise the screen 
screen = pygame.display.set_mode((800,600),0,32)
backgroundcolour = (255, 255, 255)
pygame.display.set_caption("MASTERCHEF VRBH")

#initialise colours
black = (0, 0, 0)
white = (255, 255, 255)

#Import Images
background = pygame.image.load("backgroundimage.jpg") 
firstimage = pygame.image.load("firstimage.jpg")
firstimage = pygame.transform.scale(firstimage, (300,300))
secondimage = pygame.image.load("secondimage.jpg")
secondimage = pygame.transform.scale(secondimage, (300,300))

import heapq
from sys import stdin, stdout
 
def dijkstra(adj, source, target, nodeOrder):
    INF = ((1<<63) - 1)//2
    pred = { x:x for x in adj }
    dist = { x:INF for x in adj }
    dist[ source ] = 0
    PQ = []
    heapq.heappush(PQ, [dist[ source ], source])
 
    while(PQ):
        u = heapq.heappop(PQ)  # u is a tuple [u_dist, u_id]
        u_dist = u[0]
        u_id = u[1]
        if u_dist == dist[u_id]:

            for v in adj[u_id]:
               v_id = v[0]
               w_uv = v[1]
               if dist[u_id] +  w_uv < dist[v_id]:
                   dist[v_id] = dist[u_id] + w_uv
                   heapq.heappush(PQ, [dist[v_id], v_id])
                   pred[v_id] = u_id
    else:
        st = []
        node = target
        while(True):
            st.append(str(node))
            if(node==pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        for i in path:
            nodeOrder.append(i)
 
def main(shopsToVisit, whereToGetItem, recipe, ingredientsList, recipeIngredients, totalSpent):
     
    adj = {'startnode': [('store4', 1), ('store7', 12), ('store9', 10), ('store11', 8)],
            'store1': [('store5', 17), ('store6', 18), ('store3',14), ('store8',8)],
            'store2': [('store7', 6), ('store9', 8), ('store10', 6)],
            'store3': [('store9', 12), ('store5', 12), ('store6', 13), ('store1', 14)],
            'store4': [('startnode', 1)],
            'store5': [('store1', 17), ('store3', 12), ('store9', 9), ('store6', 16), ('store8', 15), ('store11', 3)],
            'store6': [('store1', 18), ('store3', 13), ('store5', 16), ('store8', 16), ('store9', 16)],
            'store7': [('startnode', 12), ('store2', 6), ('store10', 5)],
            'store8': [('store9', 15), ('store5', 15), ('store6', 16), ('store1', 8)],
            'store9': [('store8', 15), ('startnode', 10), ('store5', 9), ('store6', 16),('store10', 5), ('store11', 7)],
            'store10': [('store9', 5), ('store7', 5), ('store2', 6)],
            'store11': [('store5', 3), ('startnode', 8), ('store9', 7)]}

    originNode = 0
    nextNode = 1
    nodeOrder = []
    totalCost = 0
    
    for s in range(1,len(shopsToVisit)):
        dijkstra(adj, shopsToVisit[originNode], shopsToVisit[nextNode], nodeOrder)
        
        if nextNode < len(shopsToVisit):
            originNode += 1
            nextNode += 1
    townMap(shopsToVisit, whereToGetItem, recipe, ingredientsList, recipeIngredients, nodeOrder, totalSpent)

def ascendingBubbleSort(unsortedList):
    length = len(unsortedList) - 1
    element = 0
    while element < length:
        if unsortedList[element] > unsortedList[element + 1]:
            hold = unsortedList[element + 1]
            unsortedList[element + 1] = unsortedList[element]
            unsortedList[element] = hold
            element = 0
        else:
            element = element + 1
    return (unsortedList)

def descendingBubbleSort(unsortedList):
    length = len(unsortedList) - 1
    element = 0
    while element < length:
        if unsortedList[element] < unsortedList[element + 1]:
            hold = unsortedList[element + 1]
            unsortedList[element + 1] = unsortedList[element]
            unsortedList[element] = hold
            element = 0
        else:
            element = element + 1
    return((unsortedList))

def ascendingQuickSort(unsortedList):
    less = []
    equal = []
    greater = []

    if len(unsortedList) > 1:
        pivot = unsortedList[0]
        for x in unsortedList:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return ascendingQuickSort(less)+equal+ascendingQuickSort(greater)
    
    else:  
        return unsortedList

def descendingQuickSort(unsortedList):
    less = []
    equal = []
    greater = []

    if len(unsortedList) > 1:
        pivot = unsortedList[0]
        for x in unsortedList:
            if x > pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x < pivot:
                greater.append(x)
        return ascendingQuickSort(less)+equal+ascendingQuickSort(greater)
    
    else:  
        return unsortedList


def mainMenu():
   #initialise the cursor
    pygame.mouse.set_visible(True)

    #Generate font objects as well as initialise and display text
    font = pg.font.SysFont("Calibri", 45, bold = True)
    newfont = pg.font.SysFont("Calibri", 35, bold = True)
    newfont1 = pg.font.SysFont("Calibri", 50, bold = True)
    greet = newfont1.render("WELCOME, ", 1, (250,0,255))
    user = newfont1.render(name, 1, (250,0,0))
    header = font.render(" TO MASTERCHEF VRBH", 1, (200,50,55))
    text = font.render("BARGAIN HUNT", 1, (0,0,255))
    groupnames = newfont.render("BY MAX, MICHAEL, NKOSILATHI, NAMAR AND ISAAC", 1, (250,0,0))

    #Generate buttons
    play = pygbutton.PygButton((350, 300, 100, 30), "Play") 
    exitgame = pygbutton.PygButton((350, 370, 100, 30), "Exit")
    
    #Responds to events such as pressing the escape key 
    while True:
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
                    
            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
                
            if 'click' in play.handleEvent(event):
                optionsScreen()
                    
        #display stuff on the screen and update it
        screen.blit(background, (0, 0))
        screen.blit(greet, (20, 30))
        screen.blit(user, (255, 30))
        screen.blit(header, (60, 80))
        screen.blit(text, (130, 120))
        screen.blit(firstimage, (5,200))
        screen.blit(secondimage, (495,200))
        screen.blit(groupnames, (15, 530))
        play.draw(screen)
        exitgame.draw(screen)
        pygame.display.update()
        
def optionsScreen():
    pygame.display.set_caption("MASTERCHEF VRBH - OPTIONS")
    pygame.mouse.set_visible(True)
    pygame.font.init()

    font = pg.font.SysFont("Calibri", 35, bold = True)
    newfont = pg.font.SysFont("Calibri", 14, bold = True)
    header = font.render("Game Options", 1, black)
    informationLabel1 = newfont.render("Play our Masterchef Virtual Robot Bargain Hunt today! All you have to do",1,black)
    informationLabel2 = newfont.render("is choose a time limit and a wallet amount, then choose your recipe that",1,black)
    informationLabel3 = newfont.render("you would like to gather the ingredients to in record time!",1, black)

    recipe1 = pygbutton.PygButton((40, 200, 160, 30), "Bacon Pasta Bake")
    recipe2 = pygbutton.PygButton((320, 200, 160, 30), "Chicken Korma")
    recipe3 = pygbutton.PygButton((600, 200, 160, 30), "Chilli Con Carne")
    recipe4 = pygbutton.PygButton((40 , 300, 160, 30), "Victoria Sandwich")
    recipe5 = pygbutton.PygButton((320, 300, 160, 30), "Lasagne")
    recipe6 = pygbutton.PygButton((600, 300, 160, 30), "Lemon Drizzle Cake")
    recipe7 = pygbutton.PygButton((40, 400, 160, 30), "Pepperoni Pizza")
    recipe8 = pygbutton.PygButton((320, 400, 160, 30), "Roast Chicken")
    recipe9 = pygbutton.PygButton((600, 400, 160, 30), "Shepherd's Pie")
    randomRecipe = pygbutton.PygButton((320, 500, 160, 30), "Random Recipe!")
    back = pygbutton.PygButton((0, 570, 70, 30), "Back")
    exitgame = pygbutton.PygButton((730, 570, 70, 30), "Exit")

    while True:
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
                    
            if 'click' in recipe1.handleEvent(event):
                recipe = 'cheesybaconpastabake.csv'
                initTownMap(recipe)
                
            if 'click' in recipe2.handleEvent(event):
                recipe = 'chickenkorma.csv'
                initTownMap(recipe)
                
            if 'click' in recipe3.handleEvent(event):
                recipe = 'chilliconcarne.csv'
                initTownMap(recipe)
                
            if 'click' in recipe4.handleEvent(event):
                recipe = 'classicvictoriasandwich.csv'
                initTownMap(recipe)
                
            if 'click' in recipe5.handleEvent(event):
                recipe = 'lasagne.csv'
                initTownMap(recipe)
                
            if 'click' in recipe6.handleEvent(event):
                recipe = 'lemondrizzlecake.csv'
                initTownMap(recipe)
                
            if 'click' in recipe7.handleEvent(event):
                recipe = 'pepperonipizza.csv'
                initTownMap(recipe)
                
            if 'click' in recipe8.handleEvent(event):
                recipe = 'roastedchickenroastpotatoes.csv'
                initTownMap(recipe)
                
            if 'click' in recipe9.handleEvent(event):
                recipe = 'shepherdspie.csv'
                initTownMap(recipe)
                
            if 'click' in randomRecipe.handleEvent(event):
                recipelist = [
                                'cheesybaconpastabake.csv', 'chickenkorma.csv', 'chilliconcarne.csv', 'classicvictoriasandwich.csv', 'lasagne.csv',
                                'lemondrizzlecake.csv', 'lemondrizzlecake.csv', 'pepperonipizza.csv', 'roastedchickenroastpotatoes.csv', 'shepherdspie.csv'
                             ]
                recipe = str(random.choice(recipelist))
                initTownMap(recipe)
                
            if 'click' in back.handleEvent(event):
                mainMenu()

            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
                    
        #display stuff on the screen and update it
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, white, (38, 28, 215, 50))
        pygame.draw.rect(screen, white, (38, 68, 440, 59))
        screen.blit(header, (40, 30))
        screen.blit(informationLabel1, (40, 70))
        screen.blit(informationLabel2, (40, 90))
        screen.blit(informationLabel3, (40, 110))
        recipe1.draw(screen)
        recipe2.draw(screen)
        recipe3.draw(screen)
        recipe4.draw(screen)
        recipe5.draw(screen)
        recipe6.draw(screen)
        recipe7.draw(screen)
        recipe8.draw(screen)
        recipe9.draw(screen)
        randomRecipe.draw(screen)
        back.draw(screen)
        exitgame.draw(screen)
        
        pygame.display.update()

def initTownMap(recipe):
    recipeIngredients = {}

    with open(recipe, 'r') as csvinput:  # this section of code pulls data from the recipe documents and converts to a dictionary
        reader = csv.reader(csvinput)
        next(reader)
        
        for row in reader:
            recipeIngredients['%s' % row[0]] = {'weight': row[1], 'quantity': row[2]}

    ingredientsList = []

    for key in recipeIngredients:
        ingredientsList.append(key)  # makes a list of JUST the ingredients needed for each recipe

    shopPrices = {}
    whereToGetItem = {} # declaring dictionaries and a list
    shopsToVisit = []
    cost = []

    for ingredients in ingredientsList:
        for i in range(1,12):
            storeNumber = 'store%d.csv' % i
            with open(storeNumber, 'r') as csvinput:
                reader = csv.reader(csvinput)
                next(reader)
                                                # this section of code finds where each ingredient is cheapest and store these values in a dictionary
                for row in reader:
                    if ingredients in row:
                        shopPrices.update({'store%d' % i: float(row[3])})
                        
        cheapestStore = min(shopPrices, key=shopPrices.get)
        cost.append(shopPrices[min(shopPrices, key=shopPrices.get)])    
        whereToGetItem.update({ingredients: cheapestStore})
        
        pos = 0
        while pos < len(shopsToVisit):
            if shopsToVisit[pos] == cheapestStore :
                break
            else:
                pos += 1
        shopsToVisit.append(cheapestStore) # this list tells the program which stores it needs to visit, hence ignoring unneeded stores

    totalSpent = ("%.2f" % round(sum(cost), 2))
    main(shopsToVisit, whereToGetItem, recipe, ingredientsList, recipeIngredients, totalSpent)

    

def townMap(shopsToVisit, whereToGetItem, recipe, ingredientsList, recipeIngredients, nodeOrder, totalSpent):

    timeCount = 0
    TREES = 0
    ROADS = 1
    GRASS = 2
    HOUSE = 3
    startnode = 4
    storeIterate = 5
    for x in range(1, 12):
        globals()['store%s' % x] = storeIterate
        storeIterate += 1
    chef = 16
    playerPosX, playerPosY = (3, 16)
        
    tiles = {
                TREES : pygame.image.load('trees.png'),
                ROADS : pygame.image.load('roads.png'),
                GRASS : pygame.image.load('grass.png'),
                HOUSE : pygame.image.load('house.png'),
                startnode: pygame.image.load('startnode.png'),
                store1 : pygame.image.load('shops.png'),
                store2 : pygame.image.load('shops.png'),
                store3 : pygame.image.load('shops.png'),
                store4 : pygame.image.load('shops.png'),
                store5 : pygame.image.load('shops.png'),
                store6 : pygame.image.load('shops.png'),
                store7 : pygame.image.load('shops.png'),
                store8 : pygame.image.load('shops.png'),
                store9 : pygame.image.load('shops.png'),
                store10 : pygame.image.load('shops.png'),
                store11 : pygame.image.load('shops.png'),
            }

    tileMap = [
                [ TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES, TREES, TREES, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, store7, GRASS, HOUSE, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES, TREES, ROADS, ROADS, ROADS, store1, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, store2, GRASS, GRASS, TREES, TREES, ROADS, GRASS, TREES, TREES, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, ROADS, GRASS, TREES, ROADS, TREES, TREES, store8, TREES, TREES, ROADS, HOUSE, TREES, TREES, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, ROADS, store10, TREES, ROADS, TREES, TREES, ROADS, ROADS, ROADS, ROADS, GRASS, TREES, TREES, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, ROADS, GRASS, HOUSE, ROADS, TREES, TREES, HOUSE, GRASS, GRASS, ROADS, GRASS, store3, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, ROADS, GRASS, TREES, ROADS, GRASS, GRASS, GRASS, GRASS, GRASS, ROADS, GRASS, ROADS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, HOUSE, ROADS, ROADS, TREES, ROADS, GRASS, GRASS, GRASS, GRASS, GRASS, ROADS, GRASS, ROADS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, store9, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, HOUSE, GRASS, TREES ],
                [ TREES, GRASS, HOUSE, ROADS, TREES, TREES, TREES, ROADS, GRASS, HOUSE, GRASS, ROADS, GRASS, HOUSE, ROADS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, TREES, ROADS, TREES, TREES, TREES, ROADS, GRASS, TREES, ROADS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, TREES, ROADS, TREES, store11, TREES, ROADS, GRASS, TREES, ROADS, HOUSE, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, TREES, ROADS, ROADS, ROADS, ROADS, ROADS, GRASS, TREES, ROADS, TREES, TREES, GRASS, GRASS, TREES ],
                [ TREES, GRASS, store4, ROADS, ROADS, ROADS, ROADS, ROADS, TREES, TREES, TREES, store5, GRASS, HOUSE, ROADS, TREES, TREES, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, startnode, HOUSE, GRASS, HOUSE, GRASS, TREES, TREES, TREES, GRASS, GRASS, GRASS, ROADS, ROADS, ROADS, store6, GRASS, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES ]
              ]

    variableNameToValue = {'startnode': 4, 'store1': 5, 'store2': 6, 'store3': 7, 'store4': 8, 'store5': 9, 'store6': 10, 'store7': 11, 'store8': 12, 'store9': 13, 'store10': 14, 'store11': 15}
    valueToVariableName = {4: 'startnode', 5: 'store1', 6: 'store2', 7: 'store3', 8: 'store4', 9: 'store5', 10: 'store6', 11: 'store7', 12: 'store8', 13: 'store9', 14: 'store10', 15: 'store11'}
    itemsGathered = defaultdict(list)
    for item, store in whereToGetItem.items():
        itemsGathered[store].append(item)
        whereToGetItem[item] = 'placeholder'

    if recipe.endswith('.csv'):
        recipe = recipe[:-4]
        
    tileSize = 30
    mapWidth = 20
    mapHeight = 20
    pygame.display.set_caption("MASTERCHEF VRBH - SIMULATION")
    displayMap = pygame.display.set_mode((800, 600))
    back = pygbutton.PygButton((0, 570, 70, 30), "Back")
    exitgame = pygbutton.PygButton((530, 570, 70, 30), "Exit")
    font3 = pg.font.SysFont("Calibri", 30, bold=False)
    font4 = pg.font.SysFont("Calibri", 20, bold=False)
    inventory = font3.render("Inventory", 1, black)
    recipe = font3.render(str(recipe), 1, black)
    inventory1 = font4.render("", 1, black)
    inventory2 = font4.render("", 1, black)
    inventory3 = font4.render("", 1, black)
    inventory4 = font4.render("", 1, black)
    inventory5 = font4.render("", 1, black)
    inventory6 = font4.render("", 1, black)
    inventory7 = font4.render("", 1, black)
    inventory8 = font4.render("", 1, black)
    pygame.draw.rect(screen, white, (600,0, 200, 600))
    pygame.draw.rect(screen, black, (600,0, 5, 600))
    pygame.draw.rect(screen, black, (600,35, 200, 2))
    pygame.draw.rect(screen, black, (600,70, 200, 2))
    chef = pygame.image.load('chef.png')
    townmap = pygame.image.load('townmap.png')
    arrow = pygame.image.load('arrow.png')
    

    iterate = True
    while True:
        for row in range(mapHeight):
            for column in range(mapWidth):
                displayMap.blit(tiles[tileMap[row][column]], (column*tileSize,row*tileSize))
                
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
                    
            if 'click' in back.handleEvent(event):
                optionsScreen()

            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()     
        back.draw(screen)
        exitgame.draw(screen)
        screen.blit(inventory, (650, 5))
        screen.blit(recipe,(650, 40))
        pygame.display.update()
        
        while iterate == True:
            
            visitedNode = []
            inventoryList = []
            value = 0
            x = 1
            
            for node in nodeOrder:
                node = variableNameToValue[node]
            
                for i in range(len(tileMap)):
                    part = tileMap[i]
                    
                    for j in range(len(part)):
                        if part[j] == node:
                            node = valueToVariableName[node]
                            
                            while playerPosX != j and playerPosY != i:
                                steps_number = max( abs(j-playerPosX), abs(i-playerPosY) )

                                stepx = float(j-playerPosX)/steps_number
                                stepy = float(i-playerPosY)/steps_number

                                for steps in range(steps_number+1):
                                    time.sleep(1)
                                    timeCount += 1
                                    screen.blit(townmap, (0, 0))
                                    screen.blit(arrow, ((j*tileSize)+3, (i*tileSize) - 27))
                                    displayMap.blit(chef, [(int(playerPosX + stepx*steps))*tileSize + 10, (int((playerPosY + stepy*steps))*tileSize) + 5])
                                    back.draw(screen)
                                    exitgame.draw(screen)
                                    pygame.display.update()
                                    
                                if node not in visitedNode:
                                    visitedNode.append(node)
                                    for key in itemsGathered:
                                        for item in (itemsGathered[key]):
                                            if node == key:
                                                inventoryList.append(itemsGathered[key][value])
                                                value += 1
                                                if x == 1:
                                                    inventory1 = font4.render(inventoryList[x-1], 1, black)
                                                elif x == 2:
                                                    inventory2 = font4.render(inventoryList[x-1], 1, black)
                                                elif x == 3:
                                                    inventory3 = font4.render(inventoryList[x-1], 1, black)
                                                elif x ==4:
                                                    inventory4 = font4.render(inventoryList[x-1], 1, black)
                                                elif x == 5:
                                                    inventory5 = font4.render(inventoryList[x-1], 1, black)
                                                elif x == 6:
                                                    inventory6 = font4.render(inventoryList[x-1], 1, black)
                                                elif x == 7:
                                                    inventory7 = font4.render(inventoryList[x-1], 1, black)
                                                elif x == 8:
                                                    inventory8 = font4.render(inventoryList[x-1], 1, black)
                                                pygame.display.update()
                                                x += 1
                                        
                                        pygame.draw.rect(screen, white, (600,0, 200, 600))
                                        pygame.draw.rect(screen, black, (600,0, 5, 600))
                                        pygame.draw.rect(screen, black, (600,35, 200, 2))
                                        pygame.draw.rect(screen, black, (600,70, 200, 2))
                                        screen.blit(inventory, (650, 5))
                                        screen.blit(recipe,(650, 40))
                                        screen.blit(inventory1, (640,100))
                                        screen.blit(inventory2, (640,140))
                                        screen.blit(inventory3, (640,180))
                                        screen.blit(inventory4, (640,220))
                                        screen.blit(inventory5, (640,260))
                                        screen.blit(inventory6, (640,300))
                                        screen.blit(inventory7, (640,340))
                                        screen.blit(inventory8, (640,380))        
                                        value = 0
                                                   
                                playerPosX, playerPosY = (j, i)
            
            iterate = False
            endScreen(ingredientsList, recipeIngredients, whereToGetItem, totalSpent, timeCount)
    
    
def endScreen(ingredientsList, recipeIngredients, whereToGetItem, totalSpent, timeCount):

    pygame.display.set_caption("MASTERCHEF VRBH - SORTING")
    unsortedList = []
    sortType = "Quick Sort"
    screen = pygame.display.set_mode((800, 600), 0, 32)
    font1 = pg.font.SysFont("Calibri", 50, bold=False)
    font2 = pg.font.SysFont("Calibri", 30, bold=False)
    font3 = pg.font.SysFont("Calibri", 20, bold=False)
    font4 = pg.font.SysFont("Calibri", 15, bold=False)
    stats = font1.render("Stats", 1, black)
    timeTaken = font2.render("Time Taken: ", 1, black)
    moneySpent = font2.render("Money Spent: ", 1, black)
    moneySpentLabel = font3.render("£ " + str(totalSpent), 1, black)
    timeCountLabel = font3.render(str(timeCount) + " seconds", 1, black)
    shoppingList = font1.render("Shopping List", 1, black)
    item = font3.render("Ingredient", 1, black)
    item1 = font4.render("", 1, black)
    item2 = font4.render("", 1, black)
    item3 = font4.render("", 1, black)
    item4 = font4.render("", 1, black)
    item5 = font4.render("", 1, black)
    item6 = font4.render("", 1, black)
    item7 = font4.render("", 1, black)
    item8 = font4.render("", 1, black)

    exitGame = pygbutton.PygButton((10, 550, 70, 30), "Exit")
    sortingOptions = pygbutton.PygButton((110, 550, 130, 30), "Quick Sort")
    ascending1 = pygbutton.PygButton((300, 510, 450, 30), "Ascending")
    descending1 = pygbutton.PygButton((300, 550, 450, 30), "Descending")

    pygame.draw.rect(screen, white, (0,0, 800, 600))
    pygame.draw.rect(screen, black, (0, 53, 800, 2))
    pygame.draw.rect(screen, black, (270, 0, 2, 600))
    pygame.draw.rect(screen, black, (0, 530, 270, 2))
    screen.blit(stats, (60, 5))
    screen.blit(shoppingList, (400, 5))
    screen.blit(timeTaken, (5, 70))
    screen.blit(moneySpent, (5, 210))
    screen.blit(moneySpentLabel, (5,250))
    screen.blit(timeCountLabel, (5, 110))
    screen.blit(item, (500, 70))
 
    exitGame.draw(screen)
    sortingOptions.draw(screen)
    ascending1.draw(screen)
    descending1.draw(screen)
    
    while True:
        iterationAsc = 0
        iterationDesc = 7
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    pygame.quit() 
                    sys.exit()
            if 'click' in exitGame.handleEvent(event):
                pygame.quit()
                sys.exit()
            if 'click' in sortingOptions.handleEvent(event):
                if sortingOptions.caption == "Quick Sort":
                    sortingOptions = pygbutton.PygButton((110, 550, 130, 30), "Bubble Sort")
                    sortType = "Bubble Sort"
                    sortingOptions.draw(screen)
                elif sortingOptions.caption == "Bubble Sort":
                    sortingOptions = pygbutton.PygButton((110, 550, 130, 30), "Quick Sort")
                    sortType = "Quick Sort"
                    sortingOptions.draw(screen)
            if 'click' in ascending1.handleEvent(event):
                pygame.draw.rect(screen, white, (272,90, 500, 400))
                unsortedList = ingredientsList 
                if sortType == "Bubble Sort":
                    ascendingBubbleSort(unsortedList)
                    item1 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item2 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item3 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item4 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item5 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item6 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item7 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item8 = font4.render(unsortedList[iterationAsc], 1, black) 
                    
                else:
                    ascendingQuickSort(unsortedList)
                    item1 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item2 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item3 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item4 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item5 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item6 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item7 = font4.render(unsortedList[iterationAsc], 1, black) 
                    iterationAsc += 1
                    item8 = font4.render(unsortedList[iterationAsc], 1, black)
                
            if 'click' in descending1.handleEvent(event):
                pygame.draw.rect(screen, white, (272,90, 500, 400))
                unsortedList = ingredientsList
                if sortType == "Bubble Sort":
                    descendingBubbleSort(unsortedList)
                    item1 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item2 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item3 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item4 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item5 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item6 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item7 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item8 = font4.render(unsortedList[iterationDesc], 1, black)
                else:
                    descendingQuickSort(unsortedList)
                    item1 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item2 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item3 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item4 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item5 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item6 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item7 = font4.render(unsortedList[iterationDesc], 1, black) 
                    iterationDesc -= 1
                    item8 = font4.render(unsortedList[iterationDesc], 1, black)
                    
            pygame.draw.rect(screen, white, (272,90, 500, 400))
            screen.blit(item1, (500,100))
            screen.blit(item2, (500,140))
            screen.blit(item3, (500,180))
            screen.blit(item4, (500,220))
            screen.blit(item5, (500,260))
            screen.blit(item6, (500,300))
            screen.blit(item7, (500,340))
            screen.blit(item8, (500,380))

            
            pygame.display.update()
mainMenu()
