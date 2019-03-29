from graphics import*
import random

def trapa(x,y,xe):
    trap = Polygon(Point(x,y),Point(x + xe*4,y),Point(x +xe*3,y+xe),Point(x + xe,y+xe))
    trap.setFill(color_rgb(200,200,200))
    trap.draw(wind)
winX = 800
wind = GraphWin("ourGraphics", winX, winX)
wind.setCoords(0, 0, 800, 800)
 
bg = Rectangle(Point(0,0), Point(winX, winX))
bg.setFill(color_rgb(255,255,255))
bg.draw(wind)

trapa(50,100,150)
