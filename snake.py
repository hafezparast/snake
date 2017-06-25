import random

tom = Turtle()
tom.shape('turtle')
tom.speed(100)
tom.ht()
size=10

def draw(x,y,c):
    tom.pu()
    tom.goto(x*size,y*size)
    tom.color(c)
    tom.pd()
    for i in range(4):
        tom.fd(size)
        tom.right(90)
        
def applyChanges(changes):
    for i in changes:
        draw(i[0],i[1],i[2])
        
        
snakes=[{'name':'A','location':[(1,1),(1,2)],'color':'green'},
        {'name':'B','location':[(-5,1),(-6,1)],'color':'blue'}]
food=(0,0)
def initiateChanges(snakes,food):
    changes=[]
    for snake in snakes:
        for x,y in snake['location']:
            changes.append((x,y,snake['color']))
    changes.append((food[0],food[1],'red'))
    return changes
                           
        
    
def gameMetrixGen(snakes,food):
    gameMatrix=[]
    for snake in snakes:
        gameMatrix+=snake['location']
    gameMatrix.append(food)
    return gameMatrix

applyChanges(initiateChanges(snakes,food))
print gameMetrixGen(snakes,food)
    
    
    

        