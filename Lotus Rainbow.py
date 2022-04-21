import turtle

turtle.title('Epic Lotus' 'Prism ')
turtle.setworldcoordinates(-2000,-2000,2000,2000)
turtle.speed(50)
turtle.bgcolor("black")
turtle.color("dark red")
turtle.pensize(1)


 #dark red
def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(1000)
        turtle.right(36)
        turtle.speed(50)
drawsign()
 
 #orange
def drawcircle(radius):
    turtle.color("#ff4400")
    turtle.pensize(1)
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(850)
        turtle.right(36)
        turtle.speed(50)
drawsign()

  #yellow (I used dark orange because my python can read yellow shades and I don't know)
def drawcircle(radius):
    turtle.color("dark orange")
    turtle.pensize(1)
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(700)
        turtle.right(36)
        turtle.speed(50)
drawsign()

#green
def drawcircle(radius):
    turtle.color("green")
    turtle.pensize(1)
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(650)
        turtle.right(36)
        turtle.speed(50)
drawsign()


def drawcircle(radius):
    turtle.color("dark blue")
    turtle.pensize(1)
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(500)
        turtle.right(36)
turtle.speed(50)
    
drawsign()

def drawcircle(radius):
    turtle.color("#4B0082")
    turtle.pensize(1)
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(450)
        turtle.right(36)
        turtle.speed(50000000)
drawsign()

def drawcircle(radius):
    turtle.color("#5200cc")
    turtle.pensize(1)
    for i in range(10):
        turtle.circle(radius)
        radius= radius+25

def drawsign():
    for i in range(10):
        drawcircle(300)
        turtle.right(36)
        turtle.speed(50000000)
drawsign()

#lotus petals
def draw_football(x,y,tilt,radius):
            turtle.speed(2000)
            turtle.color("#ff7b00")
            turtle.pensize(3)
            turtle.up()
            turtle.goto(x,y)
            turtle.down()
            turtle.seth(tilt-45)
            turtle.circle(radius,90)
            turtle.left(90)
            turtle.circle(radius,90)
    

for tilt in range(0,340,30): 
            draw_football(0,0,tilt,400)

def draw_football(x,y,tilt,radius):
            turtle.speed(2000)
            turtle.color("#8510c4")
            turtle.pensize(3)
            turtle.up()
            turtle.goto(x,y)
            turtle.down()
            turtle.seth(tilt-45)
            turtle.circle(radius,90)
            turtle.left(90)
            turtle.circle(radius,90)
       

for tilt in range(0,340,30): 
         draw_football(0,0,tilt,250)

def draw_football(x,y,tilt,radius):
            turtle.speed(2000)
            turtle.color("#ec1cff") 
            turtle.pensize(3)
            turtle.up()
            turtle.goto(x,y)
            turtle.down()
            turtle.seth(tilt-45)
            turtle.circle(radius,90)
            turtle.left(90)
            turtle.circle(radius,90)
 

for tilt in range(0,340,30): 
         draw_football(0,0,tilt,150)

turtle.hideturtle()
turtle.exitonclick()