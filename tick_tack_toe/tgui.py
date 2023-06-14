import turtle as t
from Tools import random_color


# screen = t.Screen()



def draw_x(pos):                                                                                

    turtle = t.Turtle()
    screen = t.Screen()
    turtle.shape('square')
    turtle.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=0.1)
    from main import xc_color
    turtle.color(xc_color[0])

    screen.tracer(0)

    # Go to the 'x/y'
    turtle.penup()
    turtle.goto(pos)

    # Set the turtle's speed (optional)
    turtle.pendown()
    turtle.speed(2)

    # Draw the first diagonal of the 'X'
    turtle.left(45)
    turtle.forward(10)

    # Draw the second diagonal of the 'X'
    turtle.goto(pos[0], pos[1])
    turtle.left(90)
    turtle.forward(10)
    turtle.goto(pos[0], pos[1])
    turtle.left(90)
    turtle.forward(10)
    turtle.goto(pos[0], pos[1])
    turtle.left(90)
    turtle.forward(10)
    turtle.goto(pos)

    # Hide the turtle
    turtle.hideturtle()
    screen.update()

    return turtle

   

def draw_circle(pos) :
    
    turtle = t.Turtle()
    screen = t.Screen()
    turtle.shape('square')
    turtle.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=0.1)
    from main import xc_color
    turtle.color(xc_color[1])
    
    screen.tracer(0)

    turtle.penup()
    turtle.goto(pos[0], pos[1] - 10)
    turtle.pendown()
    turtle.circle(10)
    # Hide the turtle
    turtle.hideturtle()
    screen.update()

    return turtle



def setup_canvas():
    turtle = t.Turtle()
    screen = t.Screen()
    turtle.shape('square')
    turtle.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=0.1)
    turtle.color(random_color())

    screen.setup(400 , 400)
    # screen.bgcolor(random_color()) 

    screen.tracer(0)

    #####1stLINE(VERTICAL)###
    turtle.penup()
    turtle.goto(-5 , -10)
    turtle.pendown()
    turtle.goto(-5,90)
    #########################

    #####2ndLINE(VERTICAL)###
    turtle.penup()
    turtle.goto(25 , -10)
    turtle.pendown()
    turtle.goto(25,90)
    #########################

    #####1stLINE(HORIZONTAL)###
    turtle.penup()
    turtle.goto(60 , 55)
    turtle.pendown()
    turtle.goto(-40,55)
    #########################

    #####2stLINE(VERTICAL)###
    turtle.penup()
    turtle.goto(60 , 25)
    turtle.pendown()
    turtle.goto(-40,25)
    #########################
    turtle.hideturtle()
    screen.update()

setup_canvas()

#################[AXIS]################
# screen.tracer(0)
    
# pos = 40 ,70            ####  3
# x = draw_circle(pos)
# print(x.position())

# pos = 10 , 70           ####  2
# draw_x(pos)

# pos = -20 , 70          ####  1
# draw_circle(pos)


# pos = -20 , 40           ####  4
# draw_x(pos)

# pos = 10 , 40           ####  5
# draw_x(pos)

# pos = 40 , 40           ####  6
# draw_circle(pos)


# pos = 40 , 10           ####  9
# draw_x(pos)

# pos = 10 , 10           ####  8
# draw_circle(pos)

# pos = -20 , 10           ####  7
# draw_circle(pos)

# screen.update()





# screen.exitonclick()
