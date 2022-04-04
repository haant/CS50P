score = int(input("What is your score?: "))

if score >= 90 and score <= 100:
    print("Your garde is A")
elif score >= 80 and score < 90:
    print("Your grade is B")
elif score >= 70 and score < 80:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grade is D")
else:
    print("Your grade is F")

# OR

if 90 <= score and score <= 100:
    print("Your garde is A")
elif 80 <= score and score < 90:
    print("Your grade is B")
elif 70 <= score and score < 80:
    print("Your grade is C")
elif 60 <= score and score < 70:
    print("Your grade is D")
else:
    print("Your grade is F")

# OR

if 90 <= score <= 100:
    print("Your garde is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
elif 60 <= score < 70:
    print("Your grade is D")
else:
    print("Your grade is F")

# OR

if score >= 90:
    print("Your garde is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")