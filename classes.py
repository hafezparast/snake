class Snake:
    def __init__(self,color,x,y,d,ID):
        self.color=color
        self.x=x
        self.y=y
        self.d=d
        self.ID=ID
        self.point=0
        self.growthFactor=0
    
    def move(self):
        y=self.y+(d%2)*(2-d)
        x=self.x+((d+1)%2)*(3-d)
        #if food:
            #growth(food)
        #elif nothing:
            #apply move
        #else
            #apply death


class Food:
    

class GameEnv:
    def __init__(self,top,right,down,left,blkSize):
        self.top=top
        self.right=right
        self.down=down
        self.left=left
        self.blkSize=blkSize
        self.gameOn=True
    def drawEnv(self):
        # to draw environment
        pass
    
    def play(self):
        #move all snakes
        pass
    
    def addSnake(self,snake):
        #generate an snake
        pass
    
    def killSnake(self.snakeID):
        #kill the snake
        pass
    
    def GenerateFood(self):
        #generate Food
        
