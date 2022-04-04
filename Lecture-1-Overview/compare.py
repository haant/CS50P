x = int(input("What is x?: "))
y = int(input("What is y?: "))

# x < y is a boolean experssion - Yes or No True or False
if x < y:
    print("x is less than y!")
if x > y:
    print("x is greater than y!")
if x == y:
    print("x is equal to y!")

# OR

if x < y:
    print("x is less than y!")
elif x > y:
    print("x is greater than y!")
elif x == y:
    print("x is equal to y!")

# OR

if x < y:
    print("x is less than y!")
elif x > y:
    print("x is greater than y!")
else:
    print("x is equal to y!")

# OR

if x < y or x > y:
    print("x is not equal to y!")
else:
    print("x is equal to y!")

# OR

if x != y:
    print("x is not equal to y!")
else:
    print("x is equal to y!")

# OR

if x == y:
    print("x is equal to y!")
else:
    print("x is not equal to y!")