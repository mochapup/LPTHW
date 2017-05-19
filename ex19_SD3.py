import os
from sys import argv
script, sug, cre, sugandcre, blk = argv
# Function "COFFEE PLEASE!"
def coffee_please(with_sugar,with_cream, with_sugarandcream, coffee_black):
    print(f"Hello, I would like {with_sugar + with_cream + with_sugarandcream + coffee_black} cups of coffee please")
    print(f"{with_sugar} cups with sugar")
    print(f"{with_cream} cups with cream")
    print(f"{with_sugarandcream} cups with sugar and cream")
    print(f"and {coffee_black} are black")

# input arguments
print("Coffee with sugar?", end= ' ')
sugar = int(input())
print("Coffee with cream?", end= ' ')
cream = int(input())
print("Coffee with sugar and cream?", end= ' ')
sugarandcream = int(input())
print("Coffee just black?", end= ' ')
black = int(input())
coffee_please(sugar, cream, sugarandcream, black)
# Directly giving arguments
coffee_please(10,2,4,1)
#Printing with inputs and math
coffee_please(sugar + 1, cream + 2, sugarandcream + 3, black + 4)
#Printing with math arguments
coffee_please(8 - 7, 9%3, 10 + -8, 2 * 1)
#printing with a variable
coffee = 10
coffee_please(coffee, coffee, coffee, coffee)
# Printing with multiple variables and math arguments
A = 10
B = (A * 2)
C = (B * 4)
D = (C * 8)
coffee_please(A, B, C, D)
# Printing with math and variables
coffee_please(A-1, int(A/5), A + 7, A*1)
# Printing with argv
coffee_please(int(sug), int(cre), int(sugandcre), int(blk))
# Printing with another Function
def a_function():
    coffee_please(2,4,6,8)
a_function()
# printing with a function that contains argv, math, and a variable!
def a_function2():
    coffee = 5
    coffee_please(10 + 5, (int(sug) + int(cre)), int(sugandcre), coffee + int(blk))
a_function2()
