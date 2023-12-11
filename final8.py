import pygame
import random

pygame.init()
###############################################
###############################################
# ENTER HERE THE SIZE OF THE SOURCE IMAGES
# Background
BG_IMAGE_WIDTH = 176
BG_IMAGE_HEIGHT = 224
# Characters
CH_IMAGE_WIDTH = 100
CH_IMAGE_HEIGHT = 100
STBY_IMAGE_WIDTH = 100
STBY_IMAGE_HEIGHT = 100
#Scale amount
Scale = 3
characterScale = 0.7
###############################################
###############################################

#WINDOW SIZE SET TO THE SIZE OF BG*SCALE
WINDOW_WIDTH = BG_IMAGE_WIDTH*Scale
WINDOW_HEIGHT = BG_IMAGE_HEIGHT*Scale

#SET UP THE WINDOW
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("SALUTE by 20191126 Lee Dongju")

#COLOR SHORTCUTS
WHITE = (255,255,255)

##################SOUND LOAD###################

from pygame import mixer

#Instantiate mixer
#mixer.init()

#Load audio file
music_files = ['assets/sound/1wave.mp3', 'assets/sound/2wave.mp3', 'assets/sound/salute.mp3']

#background music
mixer.music.load(music_files[0])
mixer.music.set_volume(1) #Set preferred volume
mixer.music.play(-1) #Play the music




##################IMAGE LOAD###################

#UP IMAGE LOAD
DEFAULT_CH_IMAGE_WIDTH = CH_IMAGE_WIDTH*characterScale
DEFAULT_CH_IMAGE_HEIGHT = CH_IMAGE_HEIGHT*characterScale
DEFAULT_CH_IMAGE_SIZE = (DEFAULT_CH_IMAGE_WIDTH, DEFAULT_CH_IMAGE_HEIGHT)
#load image
up1 = pygame.image.load('assets/north/n1.png')
up2 = pygame.image.load('assets/north/n2.png')
up3 = pygame.image.load('assets/north/n3.png')
up4 = pygame.image.load('assets/north/n4.png')
#size adjustment
up1 = pygame.transform.scale(up1, DEFAULT_CH_IMAGE_SIZE)
up2 = pygame.transform.scale(up2, DEFAULT_CH_IMAGE_SIZE)
up3 = pygame.transform.scale(up3, DEFAULT_CH_IMAGE_SIZE)
up4 = pygame.transform.scale(up4, DEFAULT_CH_IMAGE_SIZE)
#transparent background
up1.set_colorkey(WHITE)
up2.set_colorkey(WHITE)
up3.set_colorkey(WHITE)
up4.set_colorkey(WHITE)

#DOWN IMAGE LOAD
#load image
down1 = pygame.image.load('assets/south/s1.png')
down2 = pygame.image.load('assets/south/s2.png')
down3 = pygame.image.load('assets/south/s3.png')
down4 = pygame.image.load('assets/south/s4.png')
#size adjustment
down1 = pygame.transform.scale(down1, DEFAULT_CH_IMAGE_SIZE)
down2 = pygame.transform.scale(down2, DEFAULT_CH_IMAGE_SIZE)
down3 = pygame.transform.scale(down3, DEFAULT_CH_IMAGE_SIZE)
down4 = pygame.transform.scale(down4, DEFAULT_CH_IMAGE_SIZE)
#transparent background
down1.set_colorkey(WHITE)
down2.set_colorkey(WHITE)
down3.set_colorkey(WHITE)
down4.set_colorkey(WHITE)

#LEFT IMAGE
#load image
left1 = pygame.image.load('assets/west/w1.png')
left2 = pygame.image.load('assets/west/w2.png')
left3 = pygame.image.load('assets/west/w3.png')
left4 = pygame.image.load('assets/west/w4.png')
#size adjustment
left1 = pygame.transform.scale(left1, DEFAULT_CH_IMAGE_SIZE)
left2 = pygame.transform.scale(left2, DEFAULT_CH_IMAGE_SIZE)
left3 = pygame.transform.scale(left3, DEFAULT_CH_IMAGE_SIZE)
left4 = pygame.transform.scale(left4, DEFAULT_CH_IMAGE_SIZE)
#transparent background
left1.set_colorkey(WHITE)
left2.set_colorkey(WHITE)
left3.set_colorkey(WHITE)
left4.set_colorkey(WHITE)

#RIGHT IMAGE
#load image
right1 = pygame.image.load('assets/east/e1.png')
right2 = pygame.image.load('assets/east/e2.png')
right3 = pygame.image.load('assets/east/e3.png')
right4 = pygame.image.load('assets/east/e4.png')
#size adjustment
right1 = pygame.transform.scale(right1, DEFAULT_CH_IMAGE_SIZE)
right2 = pygame.transform.scale(right2, DEFAULT_CH_IMAGE_SIZE)
right3 = pygame.transform.scale(right3, DEFAULT_CH_IMAGE_SIZE)
right4 = pygame.transform.scale(right4, DEFAULT_CH_IMAGE_SIZE)
#transparent background
right1.set_colorkey(WHITE)
right2.set_colorkey(WHITE)
right3.set_colorkey(WHITE)
right4.set_colorkey(WHITE)

#LIST ORGANIZATION
#put images in a list
walkUp = [up1, up2, up3, up4]
walkDown = [down1, down2, down3, down4]
walkLeft = [left1, left2, left3, left4]
walkRight = [right1, right2, right3, right4]

###############################################

#STANDBY IMAGE LOAD
DEFAULT_STBY_IMAGE_SIZE = (STBY_IMAGE_WIDTH*characterScale, STBY_IMAGE_HEIGHT*characterScale)
#load image
char = pygame.image.load('assets/north/n1.png')
#size adjustment
char = pygame.transform.scale(char, DEFAULT_STBY_IMAGE_SIZE)
#transparent background
char.set_colorkey(WHITE)

###############################################

#SALUTE NORTH IMAGE LOAD
#load image
saluteNorth = pygame.image.load('assets/north/n0.png')
#size adjustment
saluteNorth = pygame.transform.scale(saluteNorth, DEFAULT_STBY_IMAGE_SIZE)
#transparent background
saluteNorth.set_colorkey(WHITE)

#SALUTE SOUTH IMAGE LOAD
#load image
saluteSouth = pygame.image.load('assets/south/s0.png')
#size adjustment
saluteSouth = pygame.transform.scale(saluteSouth, DEFAULT_STBY_IMAGE_SIZE)
#transparent background
saluteSouth.set_colorkey(WHITE)

###############################################

#BACKGROUND IMAGE LOAD
DEFAULT_BG_IMAGE_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
#load image
bg = pygame.image.load('assets/bg/ground.png')
#size adjustment
bg = pygame.transform.scale(bg, DEFAULT_BG_IMAGE_SIZE)

###############################################

#RANK IMAGE LOAD
r0 = pygame.image.load('assets/rank/r0.png')
r1 = pygame.image.load('assets/rank/r1.png')
r2 = pygame.image.load('assets/rank/r2.png')
r3 = pygame.image.load('assets/rank/r3.png')
r4 = pygame.image.load('assets/rank/r4.png')
r5 = pygame.image.load('assets/rank/r5.png')
r6 = pygame.image.load('assets/rank/r6.png')
r7 = pygame.image.load('assets/rank/r7.png')
r8 = pygame.image.load('assets/rank/r8.png')
r9 = pygame.image.load('assets/rank/r9.png')
r10 = pygame.image.load('assets/rank/r10.png')
r11 = pygame.image.load('assets/rank/r11.png')
r12 = pygame.image.load('assets/rank/r12.png')
r13 = pygame.image.load('assets/rank/r13.png')
r14 = pygame.image.load('assets/rank/r14.png')
r15 = pygame.image.load('assets/rank/r15.png')
r16 = pygame.image.load('assets/rank/r16.png')
r17 = pygame.image.load('assets/rank/r17.png')
r18 = pygame.image.load('assets/rank/r18.png')

rank_img = [r0, r1, r2, r3, 
            r4, r5, r6, r7,
            r8, r9, r10, r11, 
            r12, r13, r14, r15,
            r16, r17, r18, ]

#resize the rank images
for i in range(18):
    rank_img[i] = pygame.transform.scale(rank_img[i], (20,20))
###############################################

######################CHARACTER CONTROL#########################
clock = pygame.time.Clock()

rank = ['이등병', '일병', '상병', '병장', 
        '하사', '중사', '상사', '원사', 
        '준위', '소위', '중위', '대위',
        '소령', '중령', '대령', '준장', 
        '소장', '중장', '대장']

#######PLAYER#######
#initial position & vel & rank
x = WINDOW_WIDTH/2
y = WINDOW_HEIGHT/2
vel = 10
playerRank = rank[0]

walkCount = 0
walkCountMax = 12

#boolean
up = False
down = False
left = False
right = False
saluteUp = False
saluteDown = False
isJump = False
jumpCount = 10


#######MOBS########
#initial position & vel & rank
x0 = 100
x1 = 200
x2 = 300

y0 = 0
y1 = 0
y2 = 0
initialYPos = -(CH_IMAGE_HEIGHT*characterScale) # Y position for coming back to the top (above the Window)

y0Vel = 4 #random.randrange(4,8)
y1Vel = 4 #random.randrange(4,8)
y2Vel = 4 #random.randrange(4,8)

rank0 = rank[(random.randrange(0,18))]
rank1 = rank[(random.randrange(0,18))]
rank2 = rank[(random.randrange(0,18))]

#mob scores
#mob0Score = 10
#mob1Score = 15
#mob2Score = 20

#boolean
mobMoving = True #Link this to a certain key press for GAME START
walkCount = 0
mobWalkCount = 0
mobWalkCountMax = 12


########SALUTE CHECK##########
saluteSuccess0 = False
saluteSuccess1 = False
saluteSuccess2 = False
saluteSuccess0once = False
saluteSuccess1once = False
saluteSuccess2once = False


########SCOREBOARD#########
myScore = 0

#######################################################################################################
font_name = pygame.font.match_font('arial')

def rank_value_check(a):
    if a == rank[0]:
        rVal = 0
    elif a == rank[1]:
        rVal = 1
    elif a == rank[2]:
        rVal = 2
    elif a == rank[3]:
        rVal = 3
    elif a == rank[4]:
        rVal = 4
    elif a == rank[5]:
        rVal = 5
    elif a == rank[6]:
        rVal = 6
    elif a == rank[7]:
        rVal = 7
    elif a == rank[8]:
        rVal = 8
    elif a == rank[9]:
        rVal = 9
    elif a == rank[10]:
        rVal = 10
    elif a == rank[11]:
        rVal = 11
    elif a == rank[12]:
        rVal = 12
    elif a == rank[13]:
        rVal = 13
    elif a == rank[14]:
        rVal = 14
    elif a == rank[15]:
        rVal = 15
    elif a == rank[16]:
        rVal = 16
    elif a == rank[17]:
        rVal = 17
    elif a == rank[18]:
        rVal = 18
    return rVal

def player_rank_by_score(cScore):

    stage0 = 500
    stage1 = 800
    stage2 = 1200
    stage3 = 1700
    stage4 = 2200
    stage5 = 3000
    stage6 = 4000
    stage7 = 5000
    stage8 = 6200
    stage9 = 7500
    stage10 = 8800
    stage11 = 10300
    stage12 = 12000
    stage13 = 13000
    stage14 = 15500
    stage15 = 18000
    stage16 = 25000
    stage17 = 40000

    if cScore < stage0 :
        cRank = rank[0]
    if cScore >= stage0 and cScore < stage1:
        cRank = rank[1]
    if cScore >= stage1 and cScore < stage2:
        cRank = rank[2]
    if cScore >= stage2 and cScore < stage3:
        cRank = rank[3]
    if cScore >= stage3 and cScore < stage4:
        cRank = rank[4]
    if cScore >= stage4 and cScore < stage5:
        cRank = rank[5]
    if cScore >= stage5 and cScore < stage6:
        cRank = rank[6]
    if cScore >= stage6 and cScore < stage7:
        cRank = rank[7]
    if cScore >= stage7 and cScore < stage8:
        cRank = rank[8]
    if cScore >= stage8 and cScore < stage9:
        cRank = rank[9]
    if cScore >= stage9 and cScore < stage10:
        cRank = rank[10]
    if cScore >= stage10 and cScore < stage11:
        cRank = rank[11]
    if cScore >= stage11 and cScore < stage12:
        cRank = rank[12]
    if cScore >= stage12 and cScore < stage13:
        cRank = rank[13]
    if cScore >= stage13 and cScore < stage14:
        cRank = rank[14]
    if cScore >= stage14 and cScore < stage15:
        cRank = rank[15]
    if cScore >= stage15 and cScore < stage16:
        cRank = rank[16]
    if cScore >= stage16 and cScore < stage17:
        cRank = rank[17]
    if cScore >= stage17:
        cRank = rank[18]
    return cRank

#def music_by_rank(cRank):
    #if cRank <= 4:
        #mixer.music.load(music_files[0])
        #mixer.music.set_volume(1) #Set preferred volume
        #mixer.music.play(-1) #Play the music

    #if cRank > 4:
        #mixer.music.load(music_files[1])
        #mixer.music.set_volume(1) #Set preferred volume
        #mixer.music.play(-1) #Play the music


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def redrawGameWindow():
    global walkCount
    global mobWalkCount
    
    global x0
    global x1
    global x2
    
    global y0
    global y1
    global y2
    
    global y0Vel
    global y1Vel
    global y2Vel

    global saluteSuccess0
    global saluteSuccess1
    global saluteSuccess2

    global myScore

    #global mob0Score
    #global mob1Score
    #global mob2Score

    global playerRank
    global rank0
    global rank1
    global rank2 




    print(rank0, rank1, rank2)
    print(rank_value_check(rank0), rank_value_check(rank1), rank_value_check(rank2))

    playerRank = player_rank_by_score(myScore)

    #draw background
    win.blit(bg, (0,0))
    draw_text(win, str(myScore), 18, WINDOW_WIDTH/ 2, 10)
    #calculation for walking animation
    if walkCount + 1 >= walkCountMax:
        walkCount = 0

    if mobWalkCount + 1 >= mobWalkCountMax:
        mobWalkCount = 0

    #calculate the random X position for the mobs every frame (certain value is given at a specific point)
    randomXPos = random.randrange(10,WINDOW_WIDTH-60)

    #when mobs go over the bottom, reset its Y position to the top and random X position
    if y0 >= WINDOW_HEIGHT:
        y0 = initialYPos
        x0 = randomXPos
        y0Vel = random.randrange(4,8) 
        rank0 = rank[(random.randrange(0,18))]
    if y1 >= WINDOW_HEIGHT:
        y1 = initialYPos
        x1 = randomXPos
        y1Vel = random.randrange(4,8)
        rank1 = rank[(random.randrange(0,18))]
    if y2 >= WINDOW_HEIGHT:
        y2 = initialYPos
        x2 = randomXPos
        y2Vel = random.randrange(4,8)
        rank2 = rank[(random.randrange(0,18))]



    #when mobs go over the top, reset its random X position
    #also add score when the mob reaches to top (so that the score isn't added up while space key is being pressed)
    if y0 <= initialYPos - 1:
        myScore += 10 * rank_value_check(rank0)
        #print('x0 success', myScore)
        x0 = randomXPos
        y0Vel = random.randrange(4,8)  
        saluteSuccess0 = False #reset salute success status
        rank0 = rank[(random.randrange(0,18))] #reset rank
    if y1 <= initialYPos - 1:
        myScore += 10 * rank_value_check(rank1)
        #print('x1 success', myScore)
        x1 = randomXPos
        y1Vel = random.randrange(4,8)
        saluteSuccess1 = False #reset salute success status
        rank1 = rank[(random.randrange(0,18))] #reset rank
    if y2 <= initialYPos - 1:
        myScore += 10 * rank_value_check(rank2)
        #print('x2 success', myScore)
        x2 = randomXPos
        y2Vel = random.randrange(4,8)
        saluteSuccess2 = False #reset salute success status
        rank2 = rank[(random.randrange(0,18))] #reset rank

###########
    #print(myScore)
    #draw mobs
    if mobMoving:
        #check for salute sucess status and change its direction
        #mob0
        if saluteSuccess0 == False:
            win.blit(walkDown[mobWalkCount//3], (x0, y0))
            win.blit(rank_img[rank_value_check(rank0)], (x0, y0))
            y0 += y0Vel
        elif saluteSuccess0 == True:
            win.blit(walkUp[mobWalkCount//3], (x0, y0))
            win.blit(rank_img[rank_value_check(rank0)], (x0, y0))
            y0 -= y0Vel   
        #mob1
        if saluteSuccess1 == False:
            win.blit(walkDown[mobWalkCount//3], (x1, y1))
            win.blit(rank_img[rank_value_check(rank1)], (x1, y1))
            y1 += y1Vel
        elif saluteSuccess1 == True:
            win.blit(walkUp[mobWalkCount//3], (x1, y1))
            win.blit(rank_img[rank_value_check(rank1)], (x1, y1))
            y1 -= y1Vel
        #mob2
        if saluteSuccess2 == False:
            win.blit(walkDown[mobWalkCount//3], (x2, y2))
            win.blit(rank_img[rank_value_check(rank2)], (x2, y2))
            y2 += y2Vel
        elif saluteSuccess2 == True:
            win.blit(walkUp[mobWalkCount//3], (x2, y2))
            win.blit(rank_img[rank_value_check(rank2)], (x2, y2))
            y2 -= y2Vel

        mobWalkCount += 1

####Player movement via key press        
    #when moving
    if up:  
        win.blit(walkUp[walkCount//3], (x,y))
        win.blit(rank_img[rank_value_check(playerRank)], (x, y))
        walkCount += 1                         
    elif down:
        win.blit(walkDown[walkCount//3], (x,y))
        win.blit(rank_img[rank_value_check(playerRank)], (x, y))
        walkCount += 1
    elif left:
        win.blit(walkLeft[walkCount//3], (x,y))
        win.blit(rank_img[rank_value_check(playerRank)], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        win.blit(rank_img[rank_value_check(playerRank)], (x, y))
        walkCount += 1
    elif saluteUp:
        win.blit(saluteNorth, (x,y))
        win.blit(rank_img[rank_value_check(playerRank)], (x, y))
        walkCount = 0
    else:
        win.blit(char, (x, y))
        win.blit(rank_img[rank_value_check(playerRank)], (x, y))
        walkCount = 0
        
    #scoreboard text
    draw_text(win, str(myScore), 18, WINDOW_WIDTH/ 2, 10)
    pygame.display.update() 
    

keys = pygame.key.get_pressed()

run = True


while run:
    
    clock.tick(walkCountMax)
    #print(x,y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #range of distance 
    xRange = 20
    yRange = 20

    failScore = -100



    #music_by_rank(rank_value_check(playerRank))
        



    
    if keys[pygame.K_SPACE]:
        saluteUp = True
        #salute sound
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(music_files[2]))

        #salute success check for every mob
        if x0 >= x - xRange and x0 <= x + xRange and y0 <= y - yRange:
            if int(rank_value_check(rank0)) > int(rank_value_check(playerRank)):
                saluteSuccess0 = True   
            elif  (rank_value_check(rank0)) <= int(rank_value_check(playerRank)):
                myScore += failScore
        #else:
            #print('x0 fail')
        if x1 >= x - xRange and x1 <= x + xRange and y1 <= y - yRange:
            if int(rank_value_check(rank1)) > int(rank_value_check(playerRank)):
                saluteSuccess1 = True   
            elif  (rank_value_check(rank1)) <= int(rank_value_check(playerRank)):
                myScore += failScore 
        #else:
            #print('x1 fail')    
        if x2 >= x - xRange and x2 <= x + xRange and y2 <= y - yRange:
            if (rank_value_check(rank2)) > int(rank_value_check(playerRank)):
                saluteSuccess2 = True   
            elif  (rank_value_check(rank2)) <= int(rank_value_check(playerRank)):
                myScore += failScore
               
        #else:
            #print('x2 fail')

    elif keys[pygame.K_UP] and y >= 0: 
        y -= vel
        up = True
        down = False

    elif keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - (CH_IMAGE_HEIGHT*characterScale) - 46:
        y += vel
        up = False
        down = True
    
    elif keys[pygame.K_LEFT] and x >= 10:  
        x -= vel
        left = True
        right = False
    
    elif keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - CH_IMAGE_WIDTH*characterScale - 10:
        x += vel
        left = False
        right = True
        
    else: 
        up = False
        down = False
        left = False
        right = False
        saluteUp = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_0]:
            isJump = True
            up = False
            down = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    redrawGameWindow() 
    
    
    
pygame.quit()