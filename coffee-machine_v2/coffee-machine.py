# install prettytable_module ->python -m pip install -U prettytable
from correctinput import  Correctinput
import os
from prettytable import PrettyTable
from resourse_data import MENU , resources

table = PrettyTable()

class Order_Coffee:
    def coffee_type(self,type):
        if (cash_input + coins_input) >= MENU[order_confirm]["cost"]:
                for i in MENU[order_confirm]["ingredients"]:
                    resources[i] -=MENU[order_confirm]["ingredients"][i]
                changes = (cash_input + coins_input) - MENU[order_confirm]["cost"]
                global money
                money += MENU[order_confirm]["cost"]
                print(f'Your Change: {changes}')
                print(f'enjoy your {order_confirm}')
        else:
            print('Insuffitient Balance!')

    def show_report(self,c):
        n_list = []
        q_list = []
        for i in resources:
            n_list.append(i)
            q_list.append(resources[i])
        table.add_column('resource',n_list)                           
        table.add_column('quantity',q_list) 
        print(table)
        table.clear()

'''**************************************************[opp-area]***********************************************'''
money = 0
while True: 
    what_to_order = Correctinput()
    order_confirm = what_to_order.correctinput('What would you like to order?' , ['espresso' ,'latte' ,'cappuccino','menu'])
    
    os.system('cls')

    order_type = Order_Coffee()

    # Administration Control
    administrative_input = Correctinput()
    if order_confirm == 'menu':
        user_output = administrative_input.correctinput('A/D Settings',['report','stop','money'])
        if user_output == 'report':
            order_type.show_report(order_confirm)
            continue
        elif user_output == 'stop':
            break

        elif user_output == 'money':
            print(money)
            continue

    # Cash Payment
    cash_input = int(input('How much cash:'))
    coins_input = int(input('How much coins:'))

    # Resource Check
    x=0
    for i in resources:
        x +=resources[i]

    y=0
    for i in MENU[order_confirm]["ingredients"]:
        y +=MENU[order_confirm]["ingredients"][i]
   
    print(x)
    print(y)
    if x >= y:
        order_type.coffee_type(order_confirm)
        
    else:
            print('Sorry! Not enough resources :(')
