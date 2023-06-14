import random

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
            
    
    # print(f'{lists[0]}\n{lists[1]}\n{lists[2]}')


print('from gfunc')


    