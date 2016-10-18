'''
Created on Nov 28, 2015

@author: bahermursi
'''

class CheckDirections(object):
    def get(self, params):
        x=0 
        y=0
        if params == "UP":
            x = 0
            y =-64
        if params == "LEFT":
            x=-64
            y=0
        if params == "RIGHT":
            x=64
            y=0
        if params == "DOWN":
            y=64
            x=0
        return (x,y)
    
    def NextMove(self,snakeList,Directions):
        direc = self.get(Directions)
        nextx = direc[0] + snakeList[0][0]
        nexty = direc[1] + snakeList[0][1]
        return (nextx, nexty,Directions)