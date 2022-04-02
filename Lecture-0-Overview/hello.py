# Ask user for their name
name = input("What is your name?: ")

# Removes whitespace form string
name = name.strip()

# Capitalizes user's name
name = name.capitalize() # Capitalizes the first letter of the first word

name = name.title() # Capitalizes the first letter of every word

# Says Hello to the user
print("Hello")
print(name)

print("Hello, " + name)

print("Hello,", name)

print("Hello, ", end="")
print(name)

print("Hello,", name, sep=' ')

print("Hello, \"friend\"")

print(f"Hello, {name}")

print("Hello, {0}".format(name))

# OR

name = name.strip.title
print(f"Hello, {name}")

# OR

name = input("What is your name?: ").strip.title
print(f"Hello, {name}")
