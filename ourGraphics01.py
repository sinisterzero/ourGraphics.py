from graphics import*
import random

winX = 800
wind = GraphWin("ourGraphics", winX, winX)
wind.setCoords(0, 0, 800, 800)
 
bg = Rectangle(Point(0,0), Point(winX, winX))
bg.setFill(color_rgb(255,255,255))
bg.draw(wind)

rTri = Polygon(Point(325,650), Point(383, 720), Point(441, 650))
rTri.setFill(color_rgb(255,0,0))
rTri.draw(wind)
 

