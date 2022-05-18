import re

email = input("What is your email?: ").strip() # Eliminates white (blank) space created by teh user

if "@" in email:
    print("Valid")
else:
    print("Invalid")

# OR

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

# OR

username, domain = email.split("@")

if username: # If it has one character it will be True
    print("Valid")
else: # If it has one character it is False
    print("Invalid")

# OR 

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

# OR

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

# OR

if re.search(".*@*", email): # . indicates any character except a newline * something to left and something to right
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search(".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^\w+@\w+\.edu$", email.lower()):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^\w+@\w+\.edu$", email.lower()):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^\w+@\w+\.edu$", email, re.IGNORECASE): # Ignore the case of the input
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^\w+@(\w+\.)\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# OR 

if re.search("^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# OR

if re.search("^\w+@(\w+\.)\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")