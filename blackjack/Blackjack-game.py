from art import logo
import random
import numpy as np
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


'''**************************************************************'''
'''Defined functions'''

'''
2 unique number picker function
'''
def unique2_num(source):
    '''
    returns 2 unique nums from the source
    '''
    num_1 = random.choice(source)
    num_2 = random.choice(source)
    t = True
    while t == True:
        if num_2 == num_1:
            num_2 = random.choice(source)
        else:
            t = False
            return num_1 , num_2
# k = unique2_num(cards)

# main blackjack function 
def blackjack():
    your_cards = list(unique2_num(cards))
    print(f'your_cards {your_cards}') 
    dealer_cards = list(unique2_num(cards))
    print(f'dealer_cards {dealer_cards[0]}__')
    loop_1st = True
    # while loop_1st == True: 
    '''1111111111111111111111111111111[CONDITION-SET]1111111111111111111111111111'''
    if sum(your_cards) == 21 and sum(dealer_cards) == 21:
        return f'Draw 😒🤷‍♂️ Dealer_cards {dealer_cards}'
        
    elif sum(your_cards) == 21:
        dealer_cards = dealer_cards.append(random.choice(cards)) 
        return f'You Win 🎉😁 Blackjack Dealer cards {dealer_cards}'
            
    elif sum(dealer_cards) == 21:
        your_1st_choice = input(f'Hit OR Stand [h/s] ')
        your_cards = your_cards.append(random.choice(cards))  
        return f'Dealer Wins 😥 Blackjack Dealer cards {dealer_cards}'
    '''1111111111111111111111111111111111111111111111111111111111111111111111111111'''
       
        
    loop_2nd = True
    while loop_2nd == True:
        your_1st_choice = str(input('Hit OR Stand [h/s] '))
        while your_1st_choice not in ['h' ,'s']:
            your_1st_choice = str(input('Please type a valid input!\nHit OR Stand [h/s]   '))

        if your_1st_choice == 'h':
            your_cards.append(random.choice(cards))
            print(your_cards[-1])
        elif your_1st_choice == 's':
            dealer_cards.append(random.choice(cards))
            print(dealer_cards[-1])

        '''2222222222222222222222222[CONDITION-SET]2222222222222222222222222222222'''
        if sum(your_cards) == 21 and not sum(dealer_cards) == 21:
            return f'{your_cards}\nYou Win 🎉😁 Dealer cards {dealer_cards}'
        elif sum(your_cards) != 21 and sum(dealer_cards) == 21:
            return f'{your_cards}\nDealer Wins 🤦‍♀️ Dealer cards {dealer_cards}'

        elif sum(your_cards) >21 or sum(dealer_cards) > 21:
            if sum(your_cards) > 21:
                dealer_cards.pop()
                return f'{your_cards}\nDealer Wins 💩🤦‍♀️ Dealer cards {dealer_cards}'
            elif sum(dealer_cards) > 21:
                return f'{your_cards}\nYou Win 🎉😁 Dealer cards {dealer_cards}'
        '''2222222222222222222222222222222222222222222222222222222222222222222222222'''
        
    

'''*************************************[WORKING-PROCESS]***********************************************'''

t1 = True
while t1 == True:
    continue_game = input('Do you want to continue the game? [y/n]  ')
    while continue_game not in ['y' ,'n']:
        continue_game = input('Please type a valid input!\ncontinue the game? [y/n]  ')

    if continue_game == 'y':
        system('cls')
        print(logo)
        game_status =blackjack()
        print(game_status)
    else:
        t1 = False

#

