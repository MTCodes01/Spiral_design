import turtle as t
import random
t.getscreen()
t.penup()
t.bgcolor("black")

x=25
clst=["#ff0000","#ff0048","#ff009c","#ff00c0","#ff00ea"\
,"#fc00ff","#de00ff","#c600ff","#ae00ff","#9000ff"\
,"#7800ff","#6000ff","#4e00ff","#4200ff","#3600ff"\
,"#2400ff","#0000ff","#001eff","#0030ff","#0048ff"\
,"#0066ff","#007eff","#0096ff","#00a8ff","#00c6ff"\
,"#00e4ff","#00fcff","#00ffe4","#00ffcc","#00ffba"\
,"#00ff9c","#00ff7e","#00ff54","#00ff42","#00ff36"\
,"#00ff1e","#00ff00","#2aff00","#42ff00","#54ff00"\
,"#62ff00","#72ff00","#84ff00","#9cff00","#baff00"\
,"#e4ff00","#fff600","#ffd800","#ffba00","#ff9600"\
,"#ff8400","#ff6600","#ff4800","#ff3000","#ff2a00"]

def test(start,end,color):
    for i in range(start,end+1,5):
        t.pencolor(color)
        t.pendown()
        t.circle(i/5,steps=4)
        t.lt(5)
        t.penup()

for j in range(len(clst)):
    test(x*j,x*(j+1),clst[j])


t.exitonclick()