#1-1

local = int(input())
foreign = int(input())
course = float(input())

if ((local + foreign) >= 10 and foreign >= 1 and course >= 3.5):
    print(min(150000, 15000 + foreign*4000))
else:
    print(0)

#1-3

local = int(input())
foreign = int(input())
course = float(input())

if((local+foreign) >= 10 and course >= 3.5):
    if(foreign >= 30):
        print(min(150000, 30000 + foreign*6000))
    else:
        if(foreign >=10 and foreign <=29):
            if(course >= 4):
                print(min(150000, 20000 + foreign*5000))
            else:
                print(min(150000, 15000 + foreign*4000))
        else:
            if(foreign == 0):
                print(0)
            else:
                print(min(150000, 10000 + foreign*3000))
else:
    print(0)

#1-2
man = int(input())
woman = int(input())
hotel1 = int(input())
hotel2 = int(input())
hotel3 = int(input())
money = int(input())

import math
room = math.ceil(man/4) + math.ceil(woman/4)
cost = room*min(hotel1, hotel2, hotel3)
if (money >= cost):
    print("Hallelujah! we have", money-cost,"left.")
else:
    print("Tonight, we had better find a nice place near the street.")
