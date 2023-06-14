import turtle as t
from turtle import Screen
import Tools
import random
import time
import sys

#######

screen = Screen()
screen.title('Classic Snake')


#######

screen = Screen()
screen.title('Classic Snake')

#####  Turtle Functions:
# true = False

def left():
    head.setheading(0)
    global true
    true = True

def right():
    head.setheading(180)
    global true
    true  = True

def up():
    head.setheading(90)
    global true
    true  = True

def down():
    head.setheading(270)
    global true
    true  = True
 

########   Creating the food:
turtle_food = t.Turtle()
turtle_food.penup()
turtle_food.shape('circle')
turtle_food.shapesize(0.5, 0.5)  # Adjust the size as per your preference
    

def food():
    #### Food placement:
    turtle_food.color(Tools.random_color())
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    turtle_food.goto(x, y)

start = True

def quit():
    global start
    start = False


###########

t.listen()


t.onkey(key = 'a' , fun= right)     # Higher Order Function.
t.onkey(key = 'd' , fun= left)     # Higher Order Function.
t.onkey(key = 'w' , fun= up)     # Higher Order Function.
t.onkey(key = 's' , fun= down)     # Higher Order Function.

t.onkey(key = 'q' , fun= quit)     # Higher Order Function.

t.bgcolor('blanched almond')
 # Screen Setup 
t.setup(600 , 600)

#######  Create a new Snake:
def create_new():
    turtle = t.Turtle()
    turtle.shape('square')
    turtle.color(Tools.random_color())
    turtle.penup()
    turtle.shapesize(0.5, 0.5)  # Adjust the size as per your preference
    return turtle

#######  Checks if snake has bitten its own tail:
def has_bitten_tail():
    head_position = turtles[0].position()

    # Iterate through the body segments starting from index 1
    for segment in turtles[1:]:
        if segment.position() == head_position:
            return True

    return False


##### Display size:
screen.setup(600 , 600)
##### Creating first piece of snake body:
turtles = [create_new()]
#### Head of the snake:
head = turtles[0]

##### First three pieces of the snake:
for i in range(1, 3):
    turtle = create_new()
    turtle.goto(-10 * i, 0)
    turtles.append(turtle)
    
screen.tracer(0)

true = False

##### Places the first food:
food()

points = 0
    #######  Loop that runs the game:
def game_loop():
    global true
    global points
    ######  Points display using turtle:
    points_turtle = t.Turtle()
    points_turtle.penup()
    points_turtle.hideturtle()
    points_turtle.goto(280, 260)  # Adjust the position as per your preference

    while true:
        # global true
        screen.update()
        time.sleep(0.05)        # 0.05 sec delay in movement.

        ##### Rules to game over:
        if head.xcor() == 300 or head.ycor() == 300 or head.xcor() == -300 or head.ycor() == -300:
            true = False

        ##### Checks if snake has bitten its own tail:
        if has_bitten_tail():
            print('Bitten it\'s own tail!')
            true = False
            sys.exit(0)

        ###### Move forward snake:
        for turtle_i in range(len(turtles)-1 , 0, -1):
            pre_x = turtles[turtle_i-1].xcor()
            pre_y = turtles[turtle_i-1].ycor()
            turtles[turtle_i].goto(pre_x , pre_y)
        turtles[0].forward(10)   

        if head.distance(turtle_food) < 10:
                
                points += 1  # Increment the points
                print(points)
                points_turtle.clear()  # Clear the previous points display
                points_turtle.setpos(280, 260)  # Set the position for writing points
                points_turtle.write(f'Points: {points}', align='right', font=('Arial', 16, 'bold'))  # Display the updated points

                turtle = create_new()
                turtle.goto(turtles[-1].xcor(), turtles[-1].ycor())
                turtles.append(turtle)
                food()


screen.onkeypress(game_loop)        

screen.exitonclick()



# from Tools import Correctinput


