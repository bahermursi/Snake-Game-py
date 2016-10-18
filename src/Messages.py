'''
Created on Nov 28, 2015

@author: bahermursi
'''
import pygame
class Messages(object):
    '''
    classdocs
    '''
   
    def text_objects(self,gameDisplay,text,color):
        font = pygame.font.SysFont(None, 25)
        myText = font.render(text, True, color)
        return myText, myText.get_rect()
    
    def gameOver(self,gameDisplay,msg,color,width,height):
        myText, textRect = self.text_objects(gameDisplay,msg,color)
        textRect.center = (width / 2), (height / 2)
        gameDisplay.blit(myText, textRect)

    def myScore(self,gameDisplay,score,color):
        font=pygame.font.Font(None,30)
        scoretext=font.render("Score:"+str(score), 1 ,color)
        gameDisplay.blit(scoretext, (10, 10))
        