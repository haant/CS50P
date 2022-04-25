import csv

name = input("What is your name?: ")
home = input("What is your home?: ")

with open("students1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})