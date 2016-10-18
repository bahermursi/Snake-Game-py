import pygame
#import time
import random
import math
from NewSnake import NewSnake 
from CheckDirections import CheckDirections
from Messages import Messages 

pygame.init()
white = (255,255,255)
red = (255,0,0)
green = (0,155,0)

check = CheckDirections()
mySnake = NewSnake()

message = Messages()

display_width = 1056
display_height  = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

background = pygame.image.load("Background.png")
snakSheet = pygame.image.load("snakeImage.png")

AppleSprite = snakSheet.subsurface(pygame.Rect((0, 3*64, 64, 64)))

gameDisplay.blit(background,(0, 0))


clock = pygame.time.Clock()

def generate_vale():
    return(math.floor(random.randrange(0, display_width-64)/64)*64.0
    ,math.floor(random.randrange(0, display_height-64)/64)*64.0)
    
def gameLoop():
   
    class Directions:
        UP = "UP"
        DOWN = "DOWN"
        LEFT = "LEFT"
        RIGHT = "RIGHT"
        
    gameExit = False
    gameOver = False
   
   
    score =0
    snakeX = math.floor(display_width/2/64)*64
    snakeY = math.floor(display_height/2/64)*64
    snakeX_change = 64
    snakeY_change = 0
    
    FPS = 5

    Directions = "RIGHT"
    snakeLength = 3
    snakeList =[]
    snakeList.insert(0,([snakeX,snakeY,Directions]))
    snakeList.insert(1,([snakeX-64,snakeY,Directions]))
    snakeList.insert(2,([snakeX,snakeY,Directions]))

    (randAppleX,randAppleY) = generate_vale()
    
    mySnake.drawSnake(gameDisplay,snakSheet,snakeList,snakeLength)
    gameDisplay.fill(white)
    pygame.display.update()

    
    while not gameExit:

        message.myScore(gameDisplay,score,red)
        
        while gameOver == True:
            gameDisplay.fill(white)
            message.gameOver(gameDisplay,"Game over, press P to play again or Q to quit", red,display_width,display_height)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if Directions !="RIGHT":
                        Directions= "LEFT"
                        snakeX_change = -64
                        snakeY_change = 0
                elif event.key == pygame.K_RIGHT:
                    if Directions != "LEFT":
                        Directions= "RIGHT"
                        snakeX_change =64
                        snakeY_change = 0
                elif event.key == pygame.K_UP:
                    if Directions != "DOWN":
                        Directions= "UP"
                        snakeY_change = -64
                        snakeX_change = 0
                elif event.key == pygame.K_DOWN:
                    if Directions != "UP":
                        Directions= "DOWN"
                        snakeY_change = 64
                        snakeX_change = 0
                       
                              
        snakeX+=snakeX_change
        snakeY+= snakeY_change
            
        for i in range(len(snakeList)-1):
            if  snakeX == snakeList[i][0] and snakeY == snakeList[i][1]:
                gameOver = True
                
        
    
        if snakeX>= display_width or snakeX< 0 or snakeY  >= display_height or snakeY  < 0:
                snakeX = math.floor((snakeX % display_width) /64)*64.0
                snakeY = math.floor((snakeY % display_height)/64)*64.0
        

        snakeList.append([snakeX, snakeY,Directions])
        #gameDisplay.fill(white) 
        gameDisplay.blit(background,(0, 0))
       
              
        message.myScore(gameDisplay,score,red)
        gameDisplay.blit(AppleSprite,(randAppleX, randAppleY))

        mySnake.drawSnake(gameDisplay,snakSheet,snakeList,snakeLength) 
             
        pygame.display.update()
       
        if snakeX == randAppleX  and snakeY  == randAppleY :
            
            (randAppleX,randAppleY) = generate_vale()
            while mySnake.is_under_snake(snakeList, randAppleX, randAppleY):
                    (randAppleX,randAppleY) = generate_vale()
            
            FPS +=.25
            snakeLength+=1
            score+=10
            
        if len(snakeList) > snakeLength:
            del snakeList[0]
            
        pygame.display.update()
        clock.tick(FPS)   
    pygame.quit()
    quit()
    
#Main    
gameLoop()














