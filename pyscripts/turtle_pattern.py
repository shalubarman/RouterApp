import turtle

def drawLine (ttl, x1, y1, x2, y2):
    ttl.penup()
    ttl.goto (x1, y1)
    ttl.pendown()
    ttl.goto (x2, y2)
    ttl.penup()

def drawPentagon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    drawLine(tt1,x1,y1,x2,y2)
    drawLine(tt1,x2,y2,x3,y3)
    drawLine(tt1,x3,y3,x4,y4)
    drawLine(tt1,x4,y4,x5,y5)
    drawLine(tt1,x5,y5,x1,y1)
    
def drawCircle(x,y):
    
    turtle.penup()
    turtle.goto (x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color ('blue')
    turtle.circle (10)
    turtle.end_fill()
    
x1,y1 = 80,140
x2,y2 = 80,80
x3,y3 = 140,60
x4,y4 = 220,80
x5,y5 = 240,140

tt1 = turtle.Turtle()
tt1.color('green')
drawPentagon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
tt1.hideturtle()

drawCircle(x1,y1)
drawCircle(x2,y2)
drawCircle(x3,y3)
drawCircle(x4,y4)
drawCircle(x5,y5)

turtle.hideturtle()
turtle.done()


