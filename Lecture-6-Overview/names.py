names = []

for _ in range(3):
    name = input("What is your name?: ")
    names.append(name)

print(f"hello, {name}")

# OR

for _ in range(3):
    names.append(input("What is your name?: "))

for name in sorted(names): # Sorts the names but does not store them
    print(f"hello, {name}")

# OR

name = input("What is your name?: ")

file = open("names.txt", "w")
file.write(name) # Creates file and appends contents with input
file.close

# OR

name = input("What is your name?: ")

file = open("names.txt", "a") # 'a' will only append the contents
file.write(name)
file.close

# OR

name = input("What is your name?: ")

file = open("names.txt", "a")
file.write(f"{name}\n") # Ensure each name is seperated from one another
file.close

# OR

name = input("What is your name?: ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# READS AN EXISTING FILE

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line)

# OR

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line, end="")

# OR

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())

# OR

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# OR 

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names):
    print(f"Hello, {name}")

# OR 

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names, reverse=True): # Alphabetically reverses the names
    print(f"Hello, {name}")