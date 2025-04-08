# with open("names.txt", "r") as file:
#     lines = file.readlines()


# for line in lines:
#     # print("Hello,", line)
#     print("Hello,", line.strip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.strip())


# # Dynamic sorting
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello,",line.rstrip() )

# Static sorting
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")