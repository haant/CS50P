import sys

print("Hello, my name is", sys.argv[1])

# OR

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments!")

# OR

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])

# OR

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])

# OR

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv:
    print("Hello, my name is", arg)

# OR

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)