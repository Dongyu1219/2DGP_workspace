import turtle

def draw_circle(x,y,z):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    turtle.right(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(z)
    
turtle.shape("turtle")
draw_circle(0,0,50)
draw_circle(200,200,100)
draw_circle(100,-100,50)
