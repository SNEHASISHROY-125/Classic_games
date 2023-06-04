import turtle as t
import os
import random
import tkinter.messagebox as messagebox


screen = t.Screen()

# Set the window title
screen.title("My Turtle")


'''*******************************************[Game Function]*********************************************************'''

game_on =  True

def run_game():
    ######

    contesters = {
                    (1,'timmy')     :   [100] ,
                    (2, 'tommy')      :  [250] ,   
                    (3,'poly')    :   [400] ,
                    (4,'zen')      :   [890]  
    }

    ######
    screen = t.Screen()
    ####### Taking input:
    bet_on = screen.textinput(title='Which one do you want to bet on:' , prompt= 'if lost: - x\nelse: + 2x\nTimmy : 100$\nTommy : 250$\nPoly : 400$\nZen : 890$')
        ### Checks if its a str or int:
    if bet_on.isdigit():
        bet_on = int(bet_on)
        print("You entered an integer:", bet_on)
    else:
        print("You entered a string:", bet_on)

    ###### Gets the contesters name based on the user Input:
    for i in contesters:
        if isinstance(bet_on , int):
            if i[0] == bet_on:
                print(contesters[i])
            
        elif isinstance(bet_on , str):
            if i[1] == bet_on:
                print(contesters[i])

    ######### Random color generator:
    def random_color():
        # turtle.pensize(2)
        t.colormode(255)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)

    ########  Screen set-up ( Resolution ):
    screen.setup(width= 500 ,height=400)         ### Screen Set-Up / Display size.

    ####### Positioning:
    turtles = []
    Y =-100
    for i in range(0,4):
        turtle = t.Turtle(shape= 'turtle')
        turtle.color(random_color())
        turtle.penup()
        turtle.goto(x=-230 , y= Y)
        Y += (200/6)
        turtles.append(turtle)

    ####### Inserting turtles to contesters Dict:
    for i, m in zip(contesters, turtles):
        contesters[i].append(m)

    ####### Turtles step increment ( Randomly ):
    race_on = False

    if bet_on:
        race_on = True
        while race_on == True:
            r_t = random.choice(turtles)
            r_t.forward(random.randint(1,5))
            if r_t.xcor() > 210:
            # If one turtle reaches destination, breaks:
                winner_turtle = r_t
                race_on = False
                # print(r_t)
                # print(contesters)

    ########  User chosen turtle:
    for i in contesters:
        if bet_on in i:
            chosen_turtle = contesters[i][1]
            # print(f'Chosen_turtle: {chosen_turtle}')
        else:
            pass

    ########  Winner_turtle Name:
    for i in contesters:
        if contesters[i][1] == winner_turtle:
            winner_turtle_name = i[1]
            # print(contesters[i][1], winner_turtle_name )

    ########  Picking the winner:
    for i in contesters:
        if bet_on == winner_turtle_name:
            result = 'Your Turtle Wins'
            # break
        else:
            result = "You Lose!"


    # Display a pop-up message
    messagebox.showinfo("RESULTS", f'{result}, winner is: {winner_turtle_name}')

    # Clears the screen when finished:
    screen.clear()
    
'''*******************************************[Game]*********************************************************'''

##########  Game start & Stop:
while game_on == True:
    continue_game = screen.textinput(title= 'Continue Game ?' , prompt= '[y/n]')
    if continue_game == 'y':
        run_game()
    else:
        game_on = False 


