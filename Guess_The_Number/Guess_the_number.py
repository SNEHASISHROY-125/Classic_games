from os import system
import random
'''*****************************[Functions]*****************************************'''
def run_game(guess_num):
    chosen_num =random.choice(range(100))
    print(chosen_num)
    lives_left = lives
    guess_num = guess_num
    # print(lives_left)
    while lives_left > 0:
        if guess_num > chosen_num  :
            print('Too high!')
            lives_left -=1
            guess_num = int(input('Guess a number '))
        elif guess_num < chosen_num  :
            print('Too low!')
            lives_left -=1
            guess_num = int(input('Guess a number '))
        else:
            break
    print(guess_num)       
    if guess_num != chosen_num :
        return (f'Chosen Number {chosen_num}\nYou loose!🩴')
        
    elif guess_num == chosen_num :
        return ('You win! 🎉💃🎈🧁🍩🍨🍺')
        

'''*****************************[STEPS]*********************************************'''
t=True
while t == True:
    print('Welcome to the game🔎\nI am thinking about a number......')
# STEP:I
    game_mode = str(input('🤿 Easy_Mode -> 10 lives\n📀 Hard_Mode -> 5 lives\nChoose Game Mode [e/h]'))
    while game_mode not in ['e', 'h']:
        print('Invalid Input!')
        game_mode = str(input('Easy_Mode -> 10 lives\nHard_Mode -> 5 lives\nChoose Game Mode [e/h]'))
    if game_mode == 'e':
        lives = 10
    else:
        lives = 5
# STEP:II
    guess_num = int(input('Guess a number ⛑️  '))
    while guess_num not in range(100):
        print('Invalid Input!')
        guess_num = int(input('Guess a number'))
# STEP:III
    result = run_game(guess_num)
    print(result)
# STEP:IV
    continue_game = input('Continue the game ? [y/n]\n')
    while continue_game not in ['y','n']:
        print('Invalid Input!')
        continue_game = input('Continue the game ? [y/n]\n')
    if continue_game == 'y':
        # pass
        # continue
        system('cls')
    else:
        t = False
        