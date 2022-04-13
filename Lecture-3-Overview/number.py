x = int(input("What is x?: "))
print(f"x is {x}") # Format strings are used 

# OR

try:
    x = int(input("What is x?: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer!")

# OR

try:
    x = int(input("What is x?: "))
except ValueError:
    print("x is not an integer!")
else:
    print(f"x is {x}")

# OR

while True:
    try:
        x = int(input("What is x?: "))
    except ValueError:
        print("x is not an integer!")
    else:
        break

print(f"x is {x}")

# OR

while True:
    try:
        x = int(input("What is x?: "))
        break
    except ValueError:
        print("x is not an integer!")

print(f"x is {x}")

# OR

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x?: "))
        except ValueError:
            print("x is not an integer!")
        else:
            break
    return x

main()

# OR

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x?: "))
        except ValueError:
            print("x is not an integer!")
        else:
            return x

main()

# OR

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x?: "))
            return x
        except ValueError:
            print("x is not an integer!")

main()

# OR 

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x?: "))
        except ValueError:
            print("x is not an integer!")

main()

# OR

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x?: "))
        except ValueError:
            pass # Can be used to re-ask the same question instead of making statement

main()

# OR

def main():
    x = get_int("What is x?: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
