from os import system
import random
import turtle as t


######### Correctinput:         ( Helps user to pick correct set of input )
class Correctinput: 
    '''correctinput(msgg , x):__
    msgg -> messege to display,
    x -> Expected input, taken as a list.
    '''
    def correctinput(self, msgg ,x):
        input_1 = input(f'{msgg} {x}\n').lower()
        if isinstance(x[0], str):
            while input_1 not in x:
                input_1 = input('Invalid input!\n').lower()
        else:
            input_1 = int(input_1)
            while input_1 not in x:
                input_1 = int(input('Invalid input!\n'))
        # system('cls')
        return input_1
            

##########  Calculator:         ( Add,Sub,Mul,Div )

'''**********************[math-functions]***********************'''
def add(user_input_num1,user_input_num2):
    return user_input_num1 + user_input_num2

def sub(user_input_num1,user_input_num2):
    return user_input_num1 - user_input_num2

def mul(user_input_num1,user_input_num2):
    return user_input_num1 * user_input_num2

def div(user_input_num1,user_input_num2):
    return user_input_num1 / user_input_num2


'''**********************************[]*****************************'''
In = Correctinput()

def calculate():
    '''Mode: mode'''
    # Correctinput: mode
    user_input_mode = eval(In.correctinput('Type mode of Calculation:', ['add' ,'mul', 'sub','div']))
    
    
    # Correctinput: numbers
    user_input_num1 = float(input('Type your  Num:\n'))
    user_input_num2 = float(input('by:\n'))
    #
    return user_input_mode(user_input_num1 ,user_input_num2)


#########  Random Color Generator:      (R,G,B)
def random_color():
    # turtle.pensize(2)
    t.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)



########   Check if in x:
def ifin(value , target):
    if value in target:
        return True
    else:
        return False
    
    

