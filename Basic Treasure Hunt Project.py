import random

import math 

tx = random.randint(-100,100)
ty = random.randint(-100,100)

px = 0
py = 0


print('Welcome to the Treasure Hunt Game!' + '\n' + '\n')

print('You are on a square island that is 200 meters long and wide. A treasure was hidden randomly in this island, and if you come 3 or less meters of distance close to the treasure, then you win the game. But if you go beyond the limits of the island, you lose the game.' + '\n' + '\n' + '\n')


while -100<=px<=100 and -100<=py<=100:
    d = int(input('\n' + '# Which direction do you want to take? Type [1] for North, [2] for South, [3] for East, [4] for West' + '\n' + '\n'))

    s = int(input('\n' + '# How many steps do you want to take? Steps must be an integer between [1] to [10]' + '\n' + '\n'))

    if d != 1:
        if d != 2:
            if d != 3:
                if d !=4:
                    print('  !!! You have chosen a non-existent direction. please try again !!!' + '\n' + '\n' )

    
    if s > 10 or s < 0:
        print('  !!! You have taken too less or too many steps; please try to keep it between 1 to 10 steps !!!' + '\n' + '\n')
        

    if d == 1 and s <= 10 and s > 0:
        py = py + s
        print ('\n' + ' >>> you are',math.sqrt(px*px+py*py),'meters away from the center of the island.' + '\n' + '\n')

    if d == 2 and s <= 10 and s > 0:
        py = py - s
        print ('\n' + ' >>> you are',math.sqrt(px*px+py*py),'meters away from the center of the island.'+ '\n' + '\n')

    if d == 3 and s <= 10 and s > 0:
        px = px + s
        print ('\n' + ' >>> you are',math.sqrt(px*px+py*py),'meters away from the center of the island.' + '\n' + '\n')

    if d == 4 and s <= 10 and s > 0:
        px = px - s
        print ('\n' + ' >>> you are',math.sqrt(px*px+py*py),'meters away from the center of the island.' + '\n' + '\n')


    dx = tx - px
    dy = ty - py
    
    if math.sqrt((dx*dx)+(dy*dy))<=3:
        print ('**************************************************************' + '\n' + 'Congratulations! You found the treasure!' + '\n' + '**************************************************************')
        print ('\n' + 'thank you for playing! - S.')
        break
    
    if px > 100 or px < -100 or py > 100 or py < -100:
        print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' + '\n' + 'GAME OVER...' + '\n' + 'you fell off the island. RIP' + '\n' + 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print ('\n' + 'thanks for playing.. - S.')
        break 


