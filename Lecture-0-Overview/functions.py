# def hello():
#     print("hello")

# name = input("What is your name?: ")

# hello()

# print(name)

# OR

# def hello(to):
#     print("hello,", to)

# name = input("What is your name?: ")

# hello(name)

# OR

# def hello(to="world"):
#     print("hello,", to)

# name = input("What is your name?: ")

# hello(name)

# OR

def main():
    name = input("What is your name?: ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
