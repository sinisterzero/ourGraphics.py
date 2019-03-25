from graphics import*
import random

winX = 800
wind = GraphWin("ourGraphics", winX, winX)
wind.setCoords(0, 0, 800, 800)
 
bg = Rectangle(Point(0,0), Point(winX, winX))
bg.setFill(color_rgb(40,40,40))
bg.draw(wind)
