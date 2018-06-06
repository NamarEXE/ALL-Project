#this code follows on from nkosi's code so all imports are the same 


#import images

endscreenBackground = pygame.image.load("Images/endscreenBackground.jpg")

def endscreen():

#Locally initialise the screen
    screen = pygame.display.set_mode((1060, 680), 0, 32)
#Generate font objects as well as initialise and display text
    font1 = pg.font.SysFont("Calibri", 100, bold=True)
    font2 = pg.font.SysFont("Calibri", 70, bold=True)
    font3 = pg.font.SysFont("Calibri", 40, bold=True)
    stats = font1.render("Stats", 1, black)
    timetaken = font2.render("Time Taken", 1, black)
    moneyspent = font2.render("Money Spent", 1, black)
    shopsvisited = font2.render("Shops Visitted", 1, black)
    itemscollected = font2.render("Items Collected", 1, black)
    shoppinglist = font1.render("Shopping List", 1, black)
    
#Only 1 button needs to be generated
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
                

#display stuff on the screen and continuously update it

    screen.blit(endscreenBackground, (0,0))
    pygame.draw.rect(screen, white, (5, 5, 260, 80)) 
    screen.blit(stats, (5, 5))
    pygame.draw.rect(screen, white, (590, 5, 255, 50))
    screen.blit(shoppingList, (590, 5))
