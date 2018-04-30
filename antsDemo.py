#IanNolon
#4/29/18
#antsDemo.py

from ggame import *
from random import randint

ANTS = 10
WIDTH = 950
HEIGHT = 550

#move our ants randomly up/down and left/right
def step():
    for ant in data['antList']:
        ant.x += randint(-4,3)
        ant.y += randint(-4,3)

#putting fire ants randomly on the screen
if __name__ == '__main__':
    
    data = {}
    data['antList'] = []
    
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(20,LineStyle(1,red),red)

    for i in range(ANTS):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
