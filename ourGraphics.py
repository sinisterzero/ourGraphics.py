from graphics import*
import random     
def trapa(x,y,xe):
    trap = Polygon(Point(x,y),Point(x + xe*4,y),Point(x +xe*3,y+xe),Point(x + xe,y+xe))
    trap.setFill(color_rgb(200,200,200))
    trap.draw(wind)
def stor(x,y,xe):
    sq = Rectangle(Point(x,y), Point(x+xe*2,y+xe))
    sq.setFill(color_rgb(255,255,255))
    sq.draw(wind)
def tria(x,y,xe):
    tri = Polygon(Point(x,y),Point(x+xe*2,y),Point(x+xe,y+xe))
    tri.setFill(color_rgb(255,255,255))
    tri.draw(wind)
def story(x,y,xe):
    trapa(x,y,xe)
    stor(x+xe,y+xe,xe)
    tria(x+xe,y,xe)
winX = 800
wind = GraphWin("ourGraphics", winX, winX)
wind.setCoords(0, 0, 800, 800)
 
bg = Rectangle(Point(0,0), Point(winX, winX))
bg.setFill(color_rgb(255,255,255))
bg.draw(wind)

x = 50
y = 0
xe = 150

for i in range(4):
    story(x,y,xe)
    y += 300-(50*i+1)
    xe -= 25
    x += 50
