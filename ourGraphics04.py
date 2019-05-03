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
 
def sW(x1,y1,x2,y2,r,g,b):
    sW = Rectangle(Point(x1, y1), Point(x2, y2))
    sW.setFill(color_rgb(r,g,b))
    sW.draw(wind)
    
sW(283,400,483,450,0,255,0)
sW(345,400,420,280,0,255,0)

def Blade(x1,y1,x2,y2,r,g,b):
    Blade = Rectangle(Point(x1, y1), Point(x2, y2))
    Blade.setFill(color_rgb(r,g,b))
    Blade.draw(wind)


for i in range(8):
    Blade(325,650-((i+1)*25),345,675-((i+1)*25),255,0,0)
    Blade(420,650-((i+1)*25),440,675-((i+1)*25),255,0,0)




    
