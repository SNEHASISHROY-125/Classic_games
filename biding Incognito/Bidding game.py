from os import system
from art import logo
import art

user_log = {}
def bid():
    user_name = str(input('Bidder name:\n'))
    user_amount = int(input('How much do you want to bid:\n$'))
    user_log[user_name] = user_amount

'''
***********************************************************************************************
'''
#Step_01
print(logo)
#Step_02
#calling bid function to start
bid()
#nxt_steps
anyone_else = input('Is there anyone else too bid: [y/n]  ')
if anyone_else == 'y':
        while anyone_else == 'y':
      #Clearing the screan.       
            system('cls')
            bid()
            anyone_else = input('Is there anyone else too bid: [y/n]  ')
      #Clearing the screan.
        system('cls')
      #Looking for the highest Bid.
        for i in user_log:
                if user_log[i] == max(user_log.values()):
                    highest_bider = str(i)
      #Final Conclution.
        print(f'The highest bider is {highest_bider} with {max(user_log.values())}$ Bid.')
