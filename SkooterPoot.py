import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("poot.wav")
pygame.mixer.music.load("sound1.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

pause = False


purple = (255,0,225)
blue = (0,0,255)
green = (0, 200, 0)
car_width = 75

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SkooterPoot")
clock = pygame.time.Clock()

backgroundimg = pygame.image.load("plain_road1.png")
backgroundimg2 = pygame.image.load("road1.png")
carimg = pygame.image.load('car3.png')
carimg2 = pygame.image.load('car1.png')
treeimg = pygame.image.load('tree.png')
coneimg = pygame.image.load('traffic_cone.png')
puppyimg = pygame.image.load('puppy.png')
bushimg = pygame.image.load("roadside_bush1.png")
flowersimg = pygame.image.load("flowers1.png")
puddleimg = pygame.image.load("puddle.png")

pygame.display.set_icon(carimg2)

def quitgame():
    pygame.quit()
    quit()

    

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Objects Dodged: "+str(count), True, blue)
    gameDisplay.blit(text, (0, 0)) 

def laps ():
    font = pygame.font.SysFont(None, 25)
    text = font.render("P = Pause ", True, blue)
    gameDisplay.blit (text, (0, 25))
def quitinfo ():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Q = Quit ", True, blue)
    gameDisplay.blit (text, (0, 50))

def Scooter_Poot():
    font = pygame.font.SysFont(None, 25)
    text = font.render("High Score: 71 by KLM", True, blue)
    gameDisplay.blit(text, (600, 0))

def strtinfo1():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Skoooter Poot V1", True, blue)
    gameDisplay.blit(text, (355, 130))

def strtinfo2():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Stay on the Road!", True, blue)
    gameDisplay.blit(text, (355, 160))

def strtinfo3():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Hold on Tight!    It Gets Faster!", True, blue)
    gameDisplay.blit(text, (307, 190))
    

def highscore():
    font = pygame.font.SysFont(None, 33)
    text = font.render("Scooter Poot V1.4 BY: KLM", True, blue)
    gameDisplay.blit(text, (230, 0))    
                     
def tree (treex, treey, treeh, treew):
    gameDisplay.blit (treeimg,[treex,treey, treew, treeh])

def bush (bushx, bushy, bushh, bushw):
    gameDisplay.blit (bushimg, [bushx, bushy, bushh, bushw])
       
def flowers (flowersx, flowersy, flowersh, flowersw):
    gameDisplay.blit (flowersimg, [flowersx, flowersy, flowersh, flowersw])
def puddle (puddlex, puddley, puddleh, puddlew):
    gameDisplay.blit (puddleimg, [puddlex, puddley, puddleh, puddlew])


    
def cone (conex, coney, coneh, conew):
    gameDisplay.blit (coneimg,[conex, coney, coneh, conew])
    
def background (bgx, bgy):
    gameDisplay.blit (backgroundimg, (bgx, bgy))
def ssbackground (bgx, bgy):
    gameDisplay.blit (backgroundimg2, (bgx, bgy))

def puppy (puppyx, puppyy, puppyh, puppyw):
    gameDisplay.blit (puppyimg, [puppyx, puppyy, puppyh, puppyw])

def car(x,y):
    gameDisplay.blit(carimg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    bgx = 0
    bgy = 0
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.play(-1)
    
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()

                if event.key == pygame.K_p:
                    game_loop()

        
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        medtext = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((display_width - 400),(display_height - 300))
        gameDisplay.blit(TextSurf, TextRect)

        button("Scoot",150,450,100,50,green,bright_green,game_loop)
        button("Poot",550,450,100,50,red,bright_red,quitgame)



        pygame.display.update()
        clock.tick(15)
            

def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                action()
                            
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = (x+(w/2)), (y+(h/2))
        gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
        

def paused():

    
    bgx = 0
    bgy = 0
    pygame.mixer.music.pause()
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()

                elif event.key == pygame.K_p:
                    unpause()

        pygame.mixer.music.play(-1)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width - 400),(display_height - 300))
        gameDisplay.blit(TextSurf, TextRect)

        button("Scoot",150,450,100,50,green,bright_green,unpause)
        button("Poot",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
            


def game_intro():


    bgx = 0
    bgy = 0
    pygame.mixer.music.play(-1)
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()

        
        ssbackground(bgx, bgy)
        highscore()
        strtinfo1()
        strtinfo2()
        strtinfo3()
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Scooter Poot", largeText)
        TextRect.center = ((display_width - 375),(display_height - 300))
        gameDisplay.blit(TextSurf, TextRect)

        

        button("Scoot",150,450,100,50,green,bright_green,game_loop)
        button("Poot",550,450,100,50,red,bright_red, quitgame)



        pygame.display.update()
        clock.tick(15)
        
def game_loop():

    pygame.mixer.music.play(-1)
    global pause
    x = (display_width * .45)
    y = (display_height * .80)


    x_change = 0
    dodged = 0
    lap = 0
    quit_info = 0
                      
    bgx = 0
    bgy = 0
    bgspeed = 10
    roadl = 190
    roadr = 565
    
    cone_startx = random.randrange(roadl, roadr)
    cone_starty = -350
    cone_speed = 3
    cone_width = 40
    cone_height = 55

    tree_startx = random.randrange(25, 26)
    tree_starty = -450
    tree_speed = cone_speed
    tree_width = 75
    tree_height = 130

    bush_startx = random.randrange(55, 76)
    bush_starty = -255
    bush_speed = cone_speed
    bush_width = 110
    bush_height = 65

    puppy_startx = random.randrange(640,740)
    puppy_starty = -550
    puppy_speed = cone_speed
    puppy_width = 40
    puppy_height = 59

    flowers_startx = random.randrange(650, 700)
    flowers_starty = -345
    flowers_speed = cone_speed
    flowers_width = 78
    flowers_height = 68

    puddle_startx = random.randrange(roadl, roadr)
    puddle_starty = -250
    puddle_speed = cone_speed
    puddle_width = 85
    puddle_height = 47

    
    gameEXIT = False
    
    while not gameEXIT:

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    
                if event.key == pygame.K_p:
                    pause = True
                    paused()

                if event.key == pygame.K_q:
                    quitgame()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0


        x += x_change

        
        background(bgx, bgy)
        Scooter_Poot()

        # start roadside obstacles
        bush(bush_startx, bush_starty, bush_width, bush_height)
        bush_starty += bush_speed

        puppy(puppy_startx, puppy_starty, puppy_width, puppy_height)
        puppy_starty += puppy_speed

        flowers(flowers_startx, flowers_starty, flowers_width, flowers_height)
        flowers_starty += flowers_speed


        
        # obstacles (objectx, objecty, objecth, objectw)
        tree(tree_startx, tree_starty, tree_width, tree_height)
        tree_starty += tree_speed
        
        cone(cone_startx, cone_starty, cone_width, cone_height)
        cone_starty += cone_speed
        
        puddle(puddle_startx, puddle_starty, puddle_width, puddle_height)
        puddle_starty += puddle_speed
        
        car(x,y)
        things_dodged(dodged)
        laps()
        quitinfo()
        
        if x < 0 + 190 or x > display_width - car_width - 160:
            crash()

        if cone_starty > display_height:
            cone_starty = 0 - 350
            cone_startx = random.randrange(roadl, roadr)
            dodged += 1
            cone_speed += 0.3

        if y < cone_starty + cone_height:

            if x > cone_startx and x < cone_startx + cone_width or x + car_width > cone_startx and x + car_width < cone_startx + cone_width:
                crash()

        if puddle_starty > display_height:
            puddle_starty = 0 - 250
            puddle_startx = random.randrange(roadl, roadr)
            dodged += 1
            puddle_speed += 0.3
            
        if y < puddle_starty + puddle_height:

            if x > puddle_startx and x < puddle_startx + puddle_width or x + car_width > puddle_startx and x + car_width < puddle_startx + puddle_width:
                crash()

        if bush_starty > display_height:
            bush_starty = 0 - 255
            bush_startx = random.randrange(55, 76)
            bush_speed += 0.3

        if puppy_starty > display_height:
            puppy_starty = 0 - 550
            puppy_startx = random.randrange(640, 740)
            puppy_speed += 0.3
            
        if flowers_starty > display_height:
            flowers_starty = 0 - 345
            flowers_startx = random.randrange(650, 700)
            flowers_speed += 0.3
           
        if tree_starty > display_height:
            tree_starty = 0 - 450
            tree_startx = random.randrange(25, 26)
            tree_speed += 0.3 
            
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
quitgame()
