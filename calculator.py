#This program does a simple calculation

# This function adds two numbers

def add(x,y):
    return int(x) + int(y)

a = input("Enter your first number: ")
b = input("Enter your second number: ")

print("The sum of your two numbers is {}".format(add(a,b)))
