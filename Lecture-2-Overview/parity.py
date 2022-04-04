# Even or Odd

x = int(input("What is x?: "))

if x % 2 == 0:
    print("x is Even")
else:
    print("x is Odd")

# OR 

def main():
    x = int(input("What is x?: "))
    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

# OR

def main():
    x = int(input("What is x?: "))
    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()

# OR

def main():
    x = int(input("What is x?: "))
    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")

def is_even(n):
    return n % 2 == 0

main()
