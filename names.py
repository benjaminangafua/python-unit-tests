# Live only
# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):  
#     print(f'Hello, {name}')


# Work with file
name = input("What's your name? ")

# # file = open("names.txt", "w")
# file = open("names.txt", "a")
# # file.write(name)
# file.write(f'{name}\n')
# file.close()

with open("names.txt", "a") as file:
    file.write(f'{name}\n')

