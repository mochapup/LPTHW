# Exercise 31, study drill 2. Making my own game.
# Setting situations
print("""You are a cat. Your days are spent sleeping around the house, meowing when you are out of food, and pooping in a box.
You wake up from a nap and stretch. What do you do now?""")
print("1. Look around the house for a new place to sleep.\n2. Meow loudly to let humans know you are hungry.\n3. Go to your litter box and take a poop.")
# Define input
cativities = input("> ")
# Defining cativities 1
if cativities == "1":
    print("You look around the house for a new place to sleep.\nDo you choose the kitchen or living room?")
    room = input("> ")
    if room == "kitchen":
        print("You enter the kitchen and find a towel laying flat on the table.\nYou laydown on the towel deciding this will do.")
    elif room  == "living room":
        print("The living room is bright and warm this time of day, perfect for a cat nap.")
        print("Where do you choose to lay?\n1. Window sill\n2. The couch.")
        location = input("> ")
        if location == "1":
            print ("The window sill is warm from the sun, best place in the house for a nap.\nYou lay down and have a long and restfull nap.")
        elif location == "2":
            print("You jump on the couch and lay down on the middle cushion. This is a great place for a catnap.")
        else:
            print ("Neither of those places look too comfy. I'll nap right here.")
    else:
        print("Neither of those places sound comfy, I'll sleep in the hallway")
elif cativities == "2":
    print("You are hungry and want your human to feed you. So, you start meowing loudly.")
    print("Is your human home?")
    answer = input("> ")
    if answer == "yes":
        print("Your human hears your cries and gives you food")
    elif answer == "no":
        print("No human can feed you, you must wait for a human to return")
    else:
        print("You have no human. You must feed yourself.")
elif cativities == "3":
    print("A toilet break is needed!")
    print("You find your litter box. Do you use it?")
    answer = input("< ")
    if answer == "yes":
        print("You pooped in your box. Good job!")
    elif answer == "no":
        print("You pooed on the floor. Better luck next time!")
    else:
        print("You decide not to poop today")
else:
    print("None of those sound fun, I'll go back to sleep.")
