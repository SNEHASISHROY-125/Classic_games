from resourse_data import MENU , resources
# from resourse_data import resources
from os import system

'''***************************************************[func-area]********************************************'''

def show_resources(order):
    for i in resources:
        print(f'{i}: {resources[i]}')
        # system('cls')

def order_latte(order):
    if (cash_input + coins_input) >= 80:
        for i in MENU[order]["ingredients"]:
            resources[i] -=MENU[order]["ingredients"][i]
        changes = (cash_input + coins_input) - 80
        global money
        money += 80
        print(f'Your Change: {changes}')
        print(f'enjoy your {order}')
    else:
        print('Insuffitient Balance!')
            

def order_cappuccino(order):
    if (cash_input + coins_input) >= 130:
        for i in MENU[order]["ingredients"]:
            resources[i] -=MENU[order]["ingredients"][i]
        changes = (cash_input + coins_input) - 130
        global money
        money += 130
        print(f'Your Change: {changes}')
        print(f'enjoy your {order}')
    else:
        print('Insuffitient Balance!')


def order_espresso(order):
    if (cash_input + coins_input) >= 150:
        for i in MENU[order]["ingredients"]:
            resources[i] -=MENU[order]["ingredients"][i]
        changes = (cash_input + coins_input) - 150
        global money
        money += 150
        print(f'Your Change: {changes}')
        print(f'enjoy your {order}')
    else:
        print('Insuffitient Balance!')


'''**************************************************[opp-area]***********************************************'''
state = True
money = 0
while state == True:
    order = str(input('What would you like to order?  (espresso ,latte ,cappuccino):').lower())
    system('cls')
    while order not in ['espresso','latte','cappuccino','report','stop', 'money']:
        print('Invalid Input!')
        order = str(input('What would you like to order?  (espresso ,latte ,cappuccino):').lower())
    
    # Administration Control
    if order == 'report':
        show_resources(order)
        continue
    elif order == 'stop':
        state = False
        continue

    elif order == 'money':
        print(money)
        continue

    # Cash Payment
    cash_input = int(input('How much cash:'))
    coins_input = int(input('How much coins:'))

    # Resource Check
    x=0
    for i in resources:
        x +=resources[i]
    # print(x)

    y=0
    for i in MENU[order]["ingredients"]:
        y +=MENU[order]["ingredients"][i]
    # print(y)
   
    if x >= y:
        if order == 'espresso':
            order_espresso(order)
            # system('cls')
            # true = False

        elif order == 'latte':
            order_latte(order)
            # system('cls')

        elif order == 'cappuccino':
            order_cappuccino(order)
            
        
    else:
            print('Sorry! Not enough resources :(')

    