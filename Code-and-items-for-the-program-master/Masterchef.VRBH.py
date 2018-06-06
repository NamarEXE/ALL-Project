import pygame, sys, pygame.mixer, pygame as pg, pygbutton, inputbox 
from pygame.locals import *

#initalise pygame
pygame.init()

#initialise colours, the cursor and the window caption 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)
lime = (0,255,0)
pygame.mouse.set_visible(True)
pygame.display.set_caption("MASTERCHEF VRBH")

#Import various Images
background = pygame.image.load("Images/backgroundimage.jpg") 
firstimage = pygame.image.load("Images/firstimage.jpg")
firstimage = pygame.transform.scale(firstimage, (300,300))
secondimage = pygame.image.load("Images/secondimage.jpg")
secondimage = pygame.transform.scale(secondimage, (300,300))

recipe1 = pygame.image.load("Images/Victoria.Cake.jpg")
recipe1 = pygame.transform.scale(recipe1, (120, 120))
recipe2 = pygame.image.load("Images/Lemon.Drizzle.Cake.jpg")
recipe2 = pygame.transform.scale(recipe2, (120, 120))
recipe3 = pygame.image.load("Images/Roasted.Chicken.jpg")
recipe3 = pygame.transform.scale(recipe3, (120, 120))
recipe4 = pygame.image.load("Images/Cheesy.Bake.jpg")
recipe4 = pygame.transform.scale(recipe4, (120, 120))
recipe5 = pygame.image.load("Images/Lasagne.jpg")
recipe5 = pygame.transform.scale(recipe5, (120, 120))
recipe6 = pygame.image.load("Images/Tuna.Pasta.Bake.jpg")
recipe6 = pygame.transform.scale(recipe6, (120, 120))
recipe7 = pygame.image.load("Images/Shepherds.Pie.jpg")
recipe7 = pygame.transform.scale(recipe7, (120, 120))
recipe8 = pygame.image.load("Images/Chilli.Con.Carne.jpg")
recipe8 = pygame.transform.scale(recipe8, (120, 120))
recipe9 = pygame.image.load("Images/Pepperoni.Pizza.jpg")
recipe9 = pygame.transform.scale(recipe9, (120, 120))
recipe10 = pygame.image.load("Images/Chicken.Korma.jpg")
recipe10 = pygame.transform.scale(recipe10, (120, 120))

#Variables to store the time and money limit input by the user, globally declared so any changes made to them apply to all functions who use them
timeinput = 0
moneyinput = 0

#Import background music and play it indefinitely
bgmusic = pygame.mixer.music.load("Music/bgmusic.mp3")
pygame.mixer.music.play(-1) 

        
def mainMenu():
    #Locally initialise the screen
    screen = pygame.display.set_mode((800,600),0,32)
    #Generate font objects as well as initialise and display text
    font = pg.font.SysFont("Calibri", 85, bold = True)
    newfont = pg.font.SysFont("Calibri", 35, bold = True) 
    header = font.render("MASTERCHEF VRBH", 1, black)
    text = font.render("BARGAIN HUNT", 1, black)
    groupnames = newfont.render("BY MAX, MICHAEL, NKOSILATHI, NAMAR AND ISAAC", 1, black)

    #Generate buttons
    play = pygbutton.PygButton((350, 300, 100, 30), "PLAY") 
    options = pygbutton.PygButton((350, 370, 100, 30), "OPTIONS")
    exitgame = pygbutton.PygButton((350, 440, 100, 30), "EXIT") 
    
    #Responds to events such as pressing the escape key 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    pygame.quit() 
                    sys.exit()
            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
            #if 'click' in play.handleEvent(event):
                pygame.mixer.music.stop() 
                #Stop music then play another song or no song at all
                #then do something else once the user clicks play
            if 'click' in options.handleEvent(event):
                Options() 
                    
        #display stuff on the screen and continuously update it
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, white, (60, 50, 690, 55)) #Generate a rectangle and display it on the screen
        pygame.draw.rect(screen, white, (130, 120, 530, 55))
        pygame.draw.rect(screen, white, (15, 530, 775, 35))
        screen.blit(header, (60, 40))
        screen.blit(text, (130, 110))
        screen.blit(firstimage, (5, 200))
        screen.blit(secondimage, (495,200))
        screen.blit(groupnames, (15, 530))
        play.draw(screen)
        options.draw(screen)
        exitgame.draw(screen)
        pygame.display.update()

def Options():
    screen = pygame.display.set_mode((1060, 680), 0, 32) 
    font = pg.font.SysFont("Calibri", 100, bold = True)
    sfont = pg.font.SysFont("Calibri", 70, bold = True)
    smallfont = pg.font.SysFont("Calibri", 40, bold = True)
    smallfont.set_italic(True) 
    options = font.render("Options", 1, black)
    recipes = sfont.render("Recipes", 1, black)
    timelimit = sfont.render("Time Limit:", 1, black)
    moneylimit = sfont.render("Money Limit:", 1, black)
    message = smallfont.render("(Press return to input the desired time and money limit!)", 1, black)

    global timeinput, moneyinput

    r1 = pygbutton.PygButton((5, 250, 150, 30), "Classic Victoria Cake")
    r2 = pygbutton.PygButton((300, 250, 150, 30), "Lemon Drizzle Cake")
    r3 = pygbutton.PygButton((590, 250, 210, 30), "Roasted Chicken And Lemon")
    r4 = pygbutton.PygButton((5, 400, 215, 30), "Cheesy Bacon And Pasta Bake")
    r5 = pygbutton.PygButton((360, 400, 100, 30), "Lasagne")
    r6 = pygbutton.PygButton((610, 400, 130, 30), "Tuna Pasta Bake")
    r7 = pygbutton.PygButton((5, 550, 120, 30), "Sherpherds Pie")
    r8 = pygbutton.PygButton((260, 550, 120, 30), "Chilli Con Carne")
    r9 = pygbutton.PygButton((520, 550, 120, 30), "Pepperoni Pizza")
    r10 = pygbutton.PygButton((780, 550, 120, 30), "Chicken Korma")
    back = pygbutton.PygButton((480, 640, 80, 30), "BACK")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    pygame.quit() 
                    sys.exit()
                if event.key == K_RETURN:
                    poundsign = u"\xA3" #Used for enabling the pound sign to be displayed on the screen 
                    timeinput = inputbox.ask(screen, "PLEASE INPUT THE TIME LIMIT (FOR E.G. 325 = 3 mins and 25 secs)")
                    moneyinput = inputbox.ask(screen, "PLEASE INPUT THE MONEY LIMIT (FOR E.G. 3040 = "+poundsign+"30 and 40p)") 
            if 'click' in back.handleEvent(event):
                mainMenu()
        
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, white, (5, 5, 260, 80)) 
        screen.blit(options, (5, 5))
        pygame.draw.rect(screen, white, (5, 100, 190, 57)) 
        screen.blit(recipes, (5, 100)) 
        r1.draw(screen)
        screen.blit(recipe1, (170, 200))
        r2.draw(screen)
        screen.blit(recipe2, (460, 200)) 
        r3.draw(screen)
        screen.blit(recipe3, (810, 200)) 
        r4.draw(screen)
        screen.blit(recipe4, (230, 350)) 
        r5.draw(screen)
        screen.blit(recipe5, (475, 350))
        r6.draw(screen)
        screen.blit(recipe6, (750, 350))
        r7.draw(screen)
        screen.blit(recipe7, (130, 500))
        r8.draw(screen)
        screen.blit(recipe8, (390, 500))
        r9.draw(screen)
        screen.blit(recipe9, (650, 500))
        r10.draw(screen)
        screen.blit(recipe10, (910, 500))
        back.draw(screen)
        pygame.draw.rect(screen, red, (590, 5, 255, 50))
        pygame.draw.rect(screen, red, (590, 65, 295, 45))
        pygame.draw.rect(screen, red, (5, 165, 745, 32)) 
        screen.blit(timelimit, (590, 5))
        screen.blit(moneylimit, (590, 60))
        screen.blit(message, (5, 165))  
        
        if int(timeinput) > 0 and int(moneyinput) > 0:
            time = sfont.render(str(timeinput)+"s", 1, black)
            money = sfont.render(str(moneyinput)+"p", 1, black)
            screen.blit(time, (855, 5))
            screen.blit(money, (895, 60))
                              
        pygame.display.update() 

mainMenu() 
            
    
