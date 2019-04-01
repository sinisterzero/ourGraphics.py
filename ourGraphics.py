from graphics import*
import random     
def trapa(x,y,xe):
    trap = Polygon(Point(x,y),Point(x + xe*4,y),Point(x +xe*3,y+xe),Point(x + xe,y+xe))
    trap.setFill(color_rgb(200,200,200))
    trap.draw(wind)
def stor(x,y):
    sq = Rectangle(Point(x,y), Point(x+300,y+150))
    sq.setFill(color_rgb(255,255,255))
    sq.draw(wind)
def story(x,y,xe):
    trapa(x,y,xe)
    stor(x+xe,y+xe)
winX = 800
wind = GraphWin("ourGraphics", winX, winX)
wind.setCoords(0, 0, 800, 800)
 
bg = Rectangle(Point(0,0), Point(winX, winX))
bg.setFill(color_rgb(255,255,255))
bg.draw(wind)

x = 50
y = 100
xe = 150

for i in range(2):
    story(x,y,xe)
    y += 300
    xe -= 50
