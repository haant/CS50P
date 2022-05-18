import re

name = input("What is your name?: ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")

# OR 

if "," in name:
    last, first = name.split(", ?") # ? 0 or 1 near it 
    name = f"{first} {last}"

print(f"hello, {name}")

# OR 

matches = re.search("^.+, .+$", name)

# OR

matches = re.search("^(.+), (.+)$", name)

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")

# OR

matches = re.search("^(.+), (.+)$", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")

# OR 

matches = re.search("^(.+), (.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# OR 

if matches := re.search("^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")