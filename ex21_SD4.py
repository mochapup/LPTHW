# Functions can return something
# Defining Functions
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract (a, b):
    print (f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just the functions!")

age = add (30, 5)
height = subtract (78,4)
weight = multiply (90,2)
iq = divide (100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ, {iq}")

# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Study Drill 4: Write a simple formula, use functions to  calculate it.

formula = 15 * (9 +(7 / 2) - 2)
print ("My formula calculated ", formula)

num1 = add (10, 5)
num2 = multiply (3, 3)
num3 = subtract (10, 3)
num4 = divide (4, 2)

functionFormuia = num1 * (num2 + (num3 / num4) - 2)
print ("My function calculated ", functionFormuia)
