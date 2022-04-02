x = 1
y = 2

z = x + y

print(z)

# OR

x = input("What's x?: ")
y = input("What's y?: ")

z = int(x) + int(y) # Is needed to convert strings to number which are used in maths

print(z)

# OR

x = int(input("What's x?: "))
y = int(input("What's y?: "))


print(x + y)

# OR

x = float(input("What's x?: "))
y = float(input("What's y?: "))

# Rounding
z = round(x + y)

print(z)
print(x + y)

print(f"{z:,}") # Formats number using a comma (,)


# Division

x = float(input("What's x?: "))
y = float(input("What's y?: "))

z = round(x / y, 2)
print(z)

print(f"{z:.2f}") # The way you specfy how many digits you want to print


# Squared Functions

def main():
    x = int(input("What is x?: "))
    print("x squared is", square(x))


def square(n):
    return n * n

main()
