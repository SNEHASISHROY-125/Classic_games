import keyboard
import time


# user_pick = 0989
# while True:
   




###########   

import random
import turtle as t
def random_color():
    # turtle.pensize(2)
    t.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


###### tgui#####
xc_color = [random_color() , random_color()]

def draw_x(pos):                                                                                

    turtle = t.Turtle()
    screen = t.Screen()
    turtle.shape('square')
    turtle.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=0.1)
    # from main import xc_color
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
    # from main import xc_color
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

####### User Input ########

user_pick = None

def key_press_event(event):
    global user_pick
    user_pick = int(event.name)
    # print('Key Pressed:', user_pick)

keyboard.on_press(key_press_event)

#################

setup_canvas()

###########

lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


axis = [

            [1 , (-20 , 70)] , [2, (10 , 70)] , [3, (40 ,70)],
            [ 4, (-20 , 40)] , [5, (10 , 40)] , [6, (40 , 40)],
            [7, (-20 , 10)] , [8, (10 , 10)] , [9, (40 , 10)]

]     

i = None
conditions = [

                (lists[0][0] , lists[0][1] , lists[0][2] ) ,
                (lists[1][0] , lists[1][1] , lists[1][2] ) ,
                (lists[2][0] , lists[2][1] , lists[2][2] ) ,
                (lists[0][0] , lists[1][0] , lists[2][0] ) ,
                (lists[0][1] , lists[1][1] , lists[2][1] ) ,
                (lists[0][2] , lists[1][2] , lists[2][2] ) ,
                (lists[0][0] , lists[1][1] , lists[2][2] ) ,
                (lists[0][2] , lists[1][1] , lists[2][0] )

]                        


def who_won():
    for i in [0 , 'x']:
        # Winning Patterns
        if (lists[0][0] == lists[0][1] == lists[0][2] == i) or \
                (lists[1][0] == lists[1][1] == lists[1][2] == i) or \
                (lists[2][0] == lists[2][1] == lists[2][2] == i) or \
                (lists[0][0] == lists[1][0] == lists[2][0] == i) or \
                (lists[0][1] == lists[1][1] == lists[2][1] == i) or \
                (lists[0][2] == lists[1][2] == lists[2][2] == i) or \
                (lists[0][0] == lists[1][1] == lists[2][2] == i) or \
                (lists[0][2] == lists[1][1] == lists[2][0] == i):
            
            if i == 0:

                print('You win')
            elif i == 'x':
                print('You loose')
            return True


def computor_move():

    empty = []
    for list in lists:
        for i in list:
            if i != 'x' and i != 0:
                empty.append(i)

    place_x = random.choice(empty)

    for list in lists:
        if place_x in list:
            list[list.index(place_x)] ='x'
        ##### Draw x #####
        for num in axis:
                if num[0] == place_x:
                        draw_x(num[1])


def is_draw():
    '''
    Tells wheather all elements are int.
    Returns true/false.
    '''
    x = 0
    for list in lists:
        for element in list:
            if isinstance(element , int):
                x += element
    # print(x)
    if x != 0:
        return False
    else:
        return True

####### main.py######
game_on = True
           
while game_on :
    
    #### Checks if it's draw:
    if is_draw():
        print('Draw')
        break
    
    while user_pick is None:
        if keyboard.is_pressed('esc'):  # Change 'esc' to the desired key to trigger program exit
            print('Program Stopped')
            keyboard.unhook_all()
            break
        else:
            time.sleep(0.1)  # Adjust sleep duration as needed
            continue

    # Rest of the code goes here...
    # print('User Pick:', user_pick)
    # print(type(user_pick))
    
    # user_pick = int(t.Screen().textinput(title= None , prompt= None))  

    if user_pick in range(1, 4):
        for num in lists[0]:
            if num == user_pick:
                lists[0][lists[0].index(num)] = 0
                #### Place O 
                for num in axis:
                    if num[0] == user_pick:        
                        draw_circle(num[1])
                        # print('1st')


    if user_pick in range(4, 7):
        for num in lists[1]:
            if num == user_pick:
                lists[1][lists[1].index(num)] = 0
                #### Place O 
                for num in axis:
                    if num[0] == user_pick:
                        draw_circle(num[1])

    if user_pick in range(7, 10):
        for num in lists[2]:
            if num == user_pick:
                lists[2][lists[2].index(num)] = 0
                #### Place O 
                for num in axis:
                    if num[0] == user_pick:
                        draw_circle(num[1])

    ######### Show Matrix:
    print(f'{lists[0]}\n{lists[1]}\n{lists[2]}')

    #### Checks if it's draw:
    if is_draw():
        print('Draw')
        break

    #### check if anyone is winning:
    if who_won():
        break
    ######

    ####  Computor's Move:
    computor_move()
    ######

    #### check if anyone is winning:
    if who_won():
        break
    ######
    user_pick = None



    