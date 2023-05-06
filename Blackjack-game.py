from art import logo
import random
import numpy as np
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    your_cards = list(np.random.choice(cards, size=2))
    print(f'your_cards {your_cards}') 
    dealer_cards = list(np.random.choice(cards , size =2))
    print(f'dealer_cards {dealer_cards[0]}__')
    loop_1st = True
    while loop_1st == True: 
        if sum(your_cards) == 21 and sum(dealer_cards) == 21:
            return f'Draw 😒🤷‍♂️ Dealer_cards {dealer_cards}'
        
        elif sum(your_cards) == 21:
            dealer_cards = dealer_cards.append(random.choice(cards)) 
            return f'You Win 🎉😁 Blackjack Dealer cards {dealer_cards}'
            
        elif sum(dealer_cards) == 21:
            your_1st_choice = input(f'Hit OR Stand [h/s] ')
            your_cards = your_cards.append(random.choice(cards))  
            return f'Dealer Wins 😥 Blackjack Dealer cards {dealer_cards}'

        your_1st_choice = input(f'Hit OR Stand [h/s] ')
        
        loop_2nd = True
        while loop_2nd == True:
            if your_1st_choice == 'h':
                your_cards.append(random.choice(cards))
                dealer_cards.append(random.choice(cards))
                if sum(your_cards) == 21 and not sum(dealer_cards) == 21:
                    return f'You Win 🎉😁 Dealer cards {dealer_cards}'
                elif sum(your_cards) != 21 and sum(dealer_cards) == 21:
                    return f'Dealer Wins 🤦‍♀️ Dealer cards {dealer_cards}'

                elif sum(your_cards) >21 or sum(dealer_cards) > 21:
                    if sum(your_cards) > 21:
                        dealer_cards.pop()
                        return f'Dealer Wins 💩🤦‍♀️ Dealer cards {dealer_cards}'
                    elif sum(dealer_cards) > 21:
                        return f'You Win 🎉😁 Dealer cards {dealer_cards}'
            elif your_1st_choice == 's':
                dealer_cards.append(random.choice(cards))
                loop_2nd = False
        else:
            loop_1st = False
        
        # else:
        #     dealer_cards.extend(random.choice(cards))
        #     if sum(dealer_cards) == 21:
        #         return f'Dealer Wins 🤦‍♀️  Dealer cards {dealer_cards}'
        #     else:



    # dealer_cards = dealer_cards.extend(random.choice(cards))
    

'''************************************************************************************'''
true = True
# Inside while loop

continue_game = input('Do you want to continue the game? [y/n]  ')
if continue_game == 'y':
    game_status =blackjack()
    print(game_status)
else:
    true = False


'''**************************************************************'''
#123
#git status
#456