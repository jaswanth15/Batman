import random
r=0
print("welcome")
print("you get 5 chances to get the number")
for i in range(0,5):
    b=int(input("enter the number"))
    print("random number is",end='')
    a=random.randint(1,6)
    print(a)
    if(a==b):
        print("you won")
        break
    else:
        r=1
        pass
if(r==1):
        print("you loose")
