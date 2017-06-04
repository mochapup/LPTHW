# Exercise 30: Else and If
# Defining variables
people = 30
cars = 40
trucks = 15

# Creating branches
#  If more cars than peoples, then print
if cars > people:
    print("We should take the cars.")
# Else if less cars than people, then print
elif cars < people:
    print("We should not take the cars.")
# Else, print
else:
    print ("We can't decide.")
# If more trucks than cars, then print
if trucks > cars:
    print("That's too many trucks.")
# Else if lest trucks than cars, then print
elif trucks < cars:
    print("Maybe we could take the trucks.")
# Else, print
else:
    print("We still can't decide.")
# If mpre prople than trucks, then print
if people > trucks:
    print("Alright, let's just take the trucks")
# Else, print
else:
    print("Fine, let's stay home then.")

# SD 3
# if less trucks than people and more cars than people, then print
if  trucks < people  and cars > people:
    print("We can can fit everyone in cars.")
# if sum of trucks and cars are greater-tha-equal to people, then print
if trucks + cars >= people:
    print("We can take cars and trucks")
