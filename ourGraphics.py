from graphics import*
import random     
def trapa(x,y,xe):#roof
    trap = Polygon(Point(x,y),Point(x + xe*4,y),Point(x +xe*3,y+xe),Point(x + xe,y+xe))
    trap.setFill(color_rgb(200,200,200))
    trap.draw(wind)
def stor(x,y,xe):#block on top roof
    sq = Rectangle(Point(x,y), Point(x+xe*2,y+xe))
    sq.setFill(color_rgb(255,255,255))
    sq.draw(wind)
def tria(x,y,xe):#triangle in the middle of the roof
    tri = Polygon(Point(x,y),Point(x+xe*2,y),Point(x+xe,y+xe))
    tri.setFill(color_rgb(255,255,255))
    tri.draw(wind)
def story(x,y,xe,rt):#create one level
    trapa(x,y,xe)
    stor(x+xe,y+xe,xe)
    tria(x+xe,y,xe)
    swindow(x,y,xe,rt)
def window(x,y,xe):#window
    rec = Rectangle(Point(x,y), Point(x+10,y+xe-10))
    rec.setFill(color_rgb(0,0,0))
    rec.draw(wind)
def swindow(x,y,xe,rt):#make more window across the block
    for i in range(rt):
        window(x+(xe),(y-xe),xe)
        x += 50
    
winX = 800
wind = GraphWin("ourGraphics", winX, winX)
wind.setCoords(0, 0, 800, 800)
 
bg = Rectangle(Point(0,0), Point(winX, winX))
bg.setFill(color_rgb(255,255,255))
bg.draw(wind)

x = 100
y = 0
xe = 150
windt = 7
#create the tower
for i in range(4):
    story(x,y,xe,windt)
    y += 300-(50*i+1)
    xe -= 25
    x += 50
    windt -= 1
