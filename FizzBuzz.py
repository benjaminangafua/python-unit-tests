import sys
def main():

    for i in range(1, get_buzz()+1  ):

        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif  i%3 == 0:
            print("Fizz")
        elif  i%5 == 0:
            print("Buzz")
        else:
            print(i)


def get_buzz():
    while True:
        num = input("Enter a number: ")

        if not num.isdigit():

            sys.exit("Not a number")
        else:
            num = int(num)
            if num > 100:
                print("Too High")
            elif num < 1:
                print("Too Low")
            else:
                return num

if __name__ == "__main__":
    main()