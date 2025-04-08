import csv

# students = []

# with open("students2.csv") as file:
#     # reader = csv.reader(file) 
#     # for row in reader:
#     #     print(row[1])
#     # for name, home in reader:
#     #     students.append({"name":name, "home":home})

#     reader = csv.DictReader(file) 
#     for row in reader:
#         students.append({"name":row['name'], "home":row['home']})

# for student in sorted(students, key=lambda student:student['name']):
#     print(f"{student['name']} id from {student['home']}")

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])

    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})

