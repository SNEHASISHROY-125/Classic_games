 
from tgfunctions import *
from Tools import random_color
from tgui import *

game_on = True
           
xc_color = [random_color() , random_color()]

 

while game_on :
    user_pick = int(input('Place your move: '))
    print(user_pick)

    if user_pick in range(1, 4):
        for num in lists[0]:
            if num == user_pick:
                lists[0][lists[0].index(num)] = 0
                #### Place O 
                for num in axis:
                    if num[0] == user_pick:        
                        draw_circle(num[1])
                        print('1st')


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

    print(f'{lists[0]}\n{lists[1]}\n{lists[2]}')

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

