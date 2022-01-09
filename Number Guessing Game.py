import random

#num=random.randint(1,10)
num=4
guess=None
chances = 5

print("Minimum System Requiremens : RTX 3090 ti, Intel 12th gen i9, 32 GB RAM")

     
while not guess == num:
    
    guess=int(input("Guess an integer between 1 and 10 ---- >>  "))
    
       
    if guess == num:
        print("You Won !")
    else:
        print("Try Again !")
        chances=chances-1
        
if chances == 0:
    print("You Lose")
