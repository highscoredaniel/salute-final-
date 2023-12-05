mport pygame
pygame.init()


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


# WINDOW SIZE SET TO THE SIZE OF BG*SCALE
    WINDOW_WIDTH = BG_IMAGE_WIDTH*Scale
    WINDOW_HEIGHT = BG_IMAGE_HEIGHT*Scale
    
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("First Game")

# COLOR SHORTCUTS
    WHITE = (255,255,255)



# UP IMAGE LOAD
    DEFAULT_CH_IMAGE_SIZE = (CH_IMAGE_WIDTH*Scale, CH_IMAGE_HEIGHT*Scale)
    #load image
    up1 = pygame.image.load('assets/1.png')
    up2 = pygame.image.load('assets/2.png')
    up3 = pygame.image.load('assets/3.png')
    up4 = pygame.image.load('assets/4.png')
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

# DOWN IMAGE LOAD
    #load image
    down1 = pygame.image.load('assets/6.png')
    down2 = pygame.image.load('assets/7.png')
    down3 = pygame.image.load('assets/8.png')
    down4 = pygame.image.load('assets/9.png')
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
    
    #put up and down is list
    walkUp = [up1, up2, up3, up4]
    walkDown = [down1, down2, down3, down4]


# BACKGROUND IMAGE LOAD
    DEFAULT_BG_IMAGE_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    #load image
    bg = pygame.image.load('assets/barrack.png')
    #size adjustment
    bg = pygame.transform.scale(bg, DEFAULT_BG_IMAGE_SIZE)


# STANDBY IMAGE LOAD
    DEFAULT_STBY_IMAGE_SIZE = (STBY_IMAGE_WIDTH*Scale, STBY_IMAGE_HEIGHT*Scale)
    #load image
    char = pygame.image.load('assets/1.png')
    #size adjustment
    char = pygame.transform.scale(char, DEFAULT_STBY_IMAGE_SIZE)
    #transparent background
    char.set_colorkey(WHITE)


# Rest of the Code
    x = WINDOW_WIDTH/2
    y = WINDOW_HEIGHT/2
    width = 40
    height = 60
    vel = 5
    walkCountMax = 12
    
    clock = pygame.time.Clock()
    
    isJump = False
    jumpCount = 10
    
    left = False
    right = False
    walkCount = 0
    
    def redrawGameWindow():
        global walkCount
        
        win.blit(bg, (0,0))  
        if walkCount + 1 >= walkCountMax:
            walkCount = 0
            
        if left:  
            win.blit(walkUp[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkDown[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
            
        pygame.display.update() 
        
    
    
    run = True
    
    while run:
        clock.tick(walkCountMax)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]: #and x > vel: 
            y -= vel
            left = True
            right = False
    
        elif keys[pygame.K_DOWN]: #and x < 500 - vel - width:  
            y += vel
            left = False
            right = True
            
        else: 
            left = False
            right = False
            walkCount = 0
            
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
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
