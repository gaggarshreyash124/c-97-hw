import random


import random

number = random.randint(1,20)
chances = 0
while chances < 5 :
    guess=int(input("enter ur guess:-"))
    if guess == number:
        print("congrats u win")
        break
    elif guess<number :
        print("too bad guess a higher no.")
    else:
        print("too bad guess a lower no.")
    chances=chances+1

if not chances < 5:
    print("u lost too bad")
    
