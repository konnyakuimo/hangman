from random import random


import random
#banmen
pl_pos=1
com_pos=1
def banmen():
    print("・"*(pl_pos-1)+"P"+"・"*(30-pl_pos)+"Goal")
    print("・"*(com_pos-1)+"C"+"・"*(30-com_pos)+"Goal")

banmen()
while True:
    input("Your turn!\nPush Enter!")
    pl_pos=pl_pos+random.randint(1,6)
    if pl_pos>30:
        pl_pos=30
    banmen()
    if pl_pos==30:
        print("You win!")
        break
    input("Com's turn!\nPush Enter!")
    com_pos=com_pos+random.randint(1,6)
    if com_pos>30:
        com_pos=30
    banmen()
    if com_pos==30:
        print("Com win!")
        break