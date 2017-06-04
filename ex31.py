# Exercise 31: Making Decisions
# Printing a question
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
# Definging door input
door = input("> ")
# Defining door 1 conditions
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("Wehat do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    # Defining input
    bear = input("> ")
    # Defining bear conditions
    if bear == "1":
        print("The bear wats your face off. Good job.")
    elif bear == "2":
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
#Defining door 2 conditions
elif door == "2":
    print("You stare into the endless abyss at cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies")
    # Insanity input
    insanity = input("< ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job! ")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Goof job! ")
# Defining other door  input
else:
    print("You stumble around and fall on a knife and die. Good job!")
