# Functions and Variables.
# Defining function cheese and crackers
def Cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# directly giving arguments
print("We can just give the function numbers directly:")
Cheese_and_crackers(20,30)

# assigning arguments to variables
print("OR, we can use variables from our scripr:")
amount_of_cheese = 10
amount_of_crackers = 50

# run variables as arguments
Cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# using math as arguments
print("We can even do math inside too:")
Cheese_and_crackers(10 + 20, 5 + 6)

# using variables and math as arguments
print("And we can combine the two, variables and math:")
Cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
