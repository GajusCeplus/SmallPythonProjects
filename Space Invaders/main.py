import pygame
import random
import math

#initialization
pygame.init()

#window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("001-ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.jpg")
#bg sound
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

#Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
#playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
#Missile
#ready - cant see, fire - it fires duh
missileImg = pygame.image.load("missile.png")
missileX = 0
missileY = 480
missileY_change = 1
missile_state = "ready"

def fire(x,y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x+16, y+10))

def isCollision(enemyX,enemyY,misX,misY):
    distance = math.sqrt(math.pow(enemyX - misX,2) + math.pow(enemyY-misY,2))
    if distance < 27:
        return True
    else:
        return False

#Score
score=0
font = pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

def printScore(x,y):
    textPrint = font.render("Score: " + str(score),True,(255,255,255))
    screen.blit(textPrint, (x,y))

#game over text
over_font = pygame.font.Font("freesansbold.ttf",64)
def gameOverText():
    over_text = over_font.render("GAME OVER",True, (255,255,255))
    screen.blit(over_text, (200,250))
#Game loop
running = True
while running:
    #rgb values
    #background first then other elements
    screen.fill((0,0,0))
    #background
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            #if event.key == pygame.K_UP:
            #    playerY_change = -0.3
            #if event.key == pygame.K_DOWN:
            #    playerY_change = 0.3
            if event.key == pygame.K_SPACE:
                if missile_state is "ready":
                    missileSound = pygame.mixer.Sound("laser.wav")
                    missileSound.play()
                    missileX = playerX
                    fire(playerX,missileY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            #if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #    playerY_change = 0
        
                
    #player border check              
    playerX += playerX_change
    if playerX < 0:
            playerX=0
    elif playerX > 736:
            playerX = 736  
    #playerY += playerY_change
    
    #enemy movement
    for i in range(num_of_enemies):
        #game over
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            gameOverText()
            break 
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i] 
                
        #collision
        collision = isCollision(enemyX[i],enemyY[i],missileX,missileY)
        if collision:
            collisionSound = pygame.mixer.Sound("explosion.wav")
            collisionSound.play()
            missile_state = "ready"
            missileY = 480
            score += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)    
        enemy(enemyX[i],enemyY[i], i)
            
    #missile movement
    if missileY <= 0:
        missileY = 480
        missile_state = "ready"
    if missile_state is "fire":
        fire(missileX,missileY)
        missileY -= missileY_change
        
    
        
    player(playerX,playerY)
    printScore(textX,textY)
    pygame.display.update()
    