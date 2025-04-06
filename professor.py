import random

# def main():
    
#     generate_integer(get_level())
    
# def get_level():
#     while True:

#         try:
#             levelInput = int(input("Level: "))
#             if 1<= levelInput <= 3:
#                 return levelInput
#         except ValueError:
#             print("EEE")
#         else:
#             continue


# def generate_integer(level):
#     try:
#         score =0
#         if 1 <= level <= 3:
#             print()
#             for i in range(10):
#                 if level == 1:
#                     x= random.randint(0,9)
#                     y=random.randint(0,9)
#                 elif level == 2:
#                     x= random.randint(10,99)
#                     y=random.randint(10,99)
#                 else:
#                     x= random.randint(100,999)
#                     y=random.randint(100,999)
                
#                 trial=0
#                 while True:
#                     try:
#                         userAnswer = int(input(f'{x} + {y} = '))
#                         trial +=1
#                         if userAnswer == x+y:
#                             score +=1
#                             break
#                     except ValueError:
#                         trial +=1
#                         if trial >=3:

#                             print("EEE")
#                             print(f'{x} + {y} = {x+y}')
#                             break
#                         else:
#                             print("EEE")
#                     else:
#                         if trial  >=3:
#                             print("EEE")
#                             print(f'{x} + {y} = {x+y}')
#                             break
#                         else:
#                             print("EEE")
#             print("Score: ", score)
#     except ValueError:
#         print("EEE")


# if __name__ == "__main__":
#     main()


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        score += solve_problem(x, y)
    print("Score:", score)

def get_level():
    while True:
        level = input("Level: ")
        if level not in ["1", "2", "3"]:
            continue
        return level

def generate_integer(level):
    if level == "1":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == "2":
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def solve_problem(x, y):
    for _ in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return 0

if _name_ == "__main__":
    main()