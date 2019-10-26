import turtle
import math
radius=int(input("How big of the flower U want bby? "+" = "))
petals=int(input("How many petals do you want hon? "+" = "))

def draw_arc(b,r):
    c=2*math.pi*r
    ca=c/(360/60)
    n=int(ca/3)+1  
    l=ca/n
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))

def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)

import turtle
wn=turtle.Screen()
bob=turtle.Turtle()
wn.bgcolor("lightgreen")
bob.pensize(5)
bob.pencolor("red")
for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/petals)

wn.mainloop()
