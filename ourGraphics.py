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
        
def sW(x1,y1,x2,y2,r,g,b):
    sW = Rectangle(Point(x1, y1), Point(x2, y2))
    sW.setFill(color_rgb(r,g,b))
    sW.draw(wind)
    

def Blade(x1,y1,x2,y2,r,g,b):
    Blade = Rectangle(Point(x1, y1), Point(x2, y2))
    Blade.setFill(color_rgb(r,g,b))
    Blade.draw(wind)

    
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
for j in range(4):
    story(x,y,xe,windt)
    y += 300-(50*j+1)
    xe -= 25
    x += 50
    windt -= 1
    
sW(283,400,483,450,0,255,0)
sW(345,400,420,280,0,255,0)

rTri = Polygon(Point(325,650), Point(383, 720), Point(441, 650))
rTri.setFill(color_rgb(255,0,0))
rTri.draw(wind)

for i in range(8):
    Blade(325,650-((i+1)*25),345,675-((i+1)*25),255,0,0)
    Blade(420,650-((i+1)*25),440,675-((i+1)*25),255,0,0)
