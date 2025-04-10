from random import randint 
import sys

randomized = randint(1, 100)
chances = 5
while chances >=1:
    try:

        user_num = int(input("Guess a number: "))

        if user_num > randomized:
            print("Too high")
        elif user_num < randomized:
            print("Too low")
        else:
            print(f"Correct guess {randomized}")
            break

        chances -= 1
    except ValueError:
        sys.exit("Not a numbers")
    
