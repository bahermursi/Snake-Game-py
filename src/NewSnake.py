import pygame

class NewSnake(object):
    growsegment = []
    movedelay = 0
    
    def is_under_snake(self,snakeList,randX,randY):
        for i in range(len(snakeList)-1):
            if randX == snakeList[i][0] and randY == snakeList[i][1]:
                return True
                break;
        return False
    
    def drawSnake(self, gameDisplay, snakSheet, snakeList, snakeLength):
        tx=3
        ty=0
    
        for i in range(0,len(snakeList)):
            segment = snakeList[i]
            segx = segment[0]
            segy = segment[1]
            segDirection = segment[2]

            if i == len(snakeList)-1:
            # Head Determine the correct image
                if segDirection == "UP":
                    # Up
                    tx = 3 
                    ty = 0
                elif segDirection == "RIGHT":
                    # Right
                    tx = 4
                    ty = 0
                elif segDirection == "DOWN":
                    # Down
                    tx = 4
                    ty = 1
                elif segDirection == "LEFT":
                    # Left
                    tx = 3
                    ty = 1
            elif i == 0:   
                prevTDirec = snakeList[i+1][2]
                prevTDirec2 = snakeList[i+2][2]
                if prevTDirec == "UP" and prevTDirec2 == "LEFT" or prevTDirec == "UP" and prevTDirec2 == "RIGHT":
                    tx = 3 
                    ty = 2
                elif prevTDirec == "RIGHT" and prevTDirec2 == "DOWN" or prevTDirec == "RIGHT" and prevTDirec2 == "UP":
                    tx = 4
                    ty = 2;
                elif prevTDirec == "LEFT" and prevTDirec2 == "DOWN" or prevTDirec == "LEFT" and prevTDirec2 == "UP":
                    tx = 3
                    ty = 3
                elif prevTDirec == "DOWN" and prevTDirec2 == "LEFT" or prevTDirec == "DOWN" and prevTDirec2 == "RIGHT":
                    tx = 4
                    ty = 3
                if prevTDirec == "UP" and prevTDirec2 == "UP":
                    # UPTail
                    tx = 3 
                    ty = 2
                elif prevTDirec == "RIGHT" and prevTDirec2 == "RIGHT" :
                    # RightTail
                    tx = 4
                    ty = 2;
                elif prevTDirec == "DOWN" and prevTDirec == "DOWN":
                    # DownTail
                    tx = 4
                    ty = 3
                elif prevTDirec == "LEFT" and prevTDirec2 == "LEFT" :
                    # Left
                    tx = 3
                    ty = 3   
            else:
                nextDirec = snakeList[i+1][2]
                prevDirec = snakeList[i][2]

                if prevDirec == "RIGHT" and nextDirec =="UP" or prevDirec == "DOWN" and nextDirec =="LEFT":
                    tx=2
                    ty=2
                elif prevDirec == "RIGHT" and nextDirec =="DOWN" or  prevDirec == "UP" and  nextDirec =="LEFT" :
                    tx=2
                    ty=0
                elif prevDirec == "LEFT" and nextDirec =="DOWN" or prevDirec == "UP" and nextDirec =="RIGHT":
                    tx=0
                    ty=0
                elif prevDirec == "DOWN" and nextDirec =="RIGHT" or prevDirec == "LEFT" and nextDirec =="UP":
                    tx=0
                    ty=1
                elif prevDirec == "RIGHT" and nextDirec =="RIGHT" or  prevDirec == "LEFT" and nextDirec =="LEFT":
                    tx=1
                    ty=0 
                elif prevDirec == "RIGHT" and nextDirec =="DOWN" or  prevDirec == "LEFT" and nextDirec =="DOWN":
                    tx=1
                    ty=0 
                elif prevDirec == "RIGHT" and nextDirec =="UP" or  prevDirec == "LEFT" and nextDirec =="UP":
                    tx=1
                    ty=0 
                elif nextDirec =="UP" and prevDirec == "UP" or nextDirec =="DOWN" and prevDirec == "DOWN":
                    tx = 2
                    ty = 1
                elif nextDirec =="LEFT" and prevDirec == "UP" or nextDirec =="RIGHT" and prevDirec == "UP":
                    tx = 2
                    ty = 1
                elif nextDirec =="LEFT" and prevDirec == "DOWN" or nextDirec =="RIGHT" and prevDirec == "DOWN":
                    tx = 2
                    ty = 1
            smallSprite = snakSheet.subsurface(pygame.Rect((tx * 64, ty * 64, 64, 64)))
            gameDisplay.blit(smallSprite, (segx, segy))