import random
i=0
while True:
    num1=random.randint(1,100)
    print(num1)
    i+=1
    if num1==77:
        print(i,"回目で当たり")
        break
    