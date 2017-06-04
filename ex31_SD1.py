# Exercise 31: Making Decisions
# Printing a question
print("""You enter a dark room with two doors.
Do you go through door #1, #2, or #3?""")
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
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job! ")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Goof job! ")
# Defining door #3 conditions
if door == "3":
    print("You walk in the find a badger, a wizard, and a podcaster sitting at a table.")
    print("what do you do?")
    print("1. Sit at the table.")
    print("2. Just stare.")
    choice = input("> ")
    if choice == "1":
        print("You sit at the table, and listen ramblings of Hello from the Magic Tavern.")
        print("Eventually you are recruited to help the wizard on his quest. Good job.")
    elif choice == "2":
        print("You stare mouth-gapping at the scene before you.")
        print(f"You've decided that choosing {choice} was a terrible decission.")
        print("You jump out the nearest window, to be never seen again")
    else:
        print ("The table stares at you quitely.")
        print("The badger asks, \"Chunts up with that?\"")
# Defining other door  input
else:
    print("You stumble around and fall on a knife and die. Good job!")
