# ex37.py
# This program is game called "Dog Park". The objective of the game is to get your dogs reduce your dogs energy with activities in the park.
# If you decrease your dogs energy too much he will pass out. Exit the park to end the game and see how well you did to decrease your dogs energy.

#Import exit function
from sys import exit

# This function activates when your dogs energy is <0
def passout(why):
    print(why, "Poor doggo.")
    exit()

dogEnergy = 150

# Defining entrance area, this is where you start the game
def entrance():
    global dogEnergy
    print("You are at the park's entrance.")
    print("You can Walk around the park, go to the Big Lawn, go to the Pine Woods, or exit the park to leave.")
    choice = input("> ")

    if "walk" in choice:
        walkEnergy = 20
        print("You and your dog take a walk on a trail around the park. This uses 20 energy.")
        dogEnergy = dogEnergy - walkEnergy
        print(f"Your dog has {dogEnergy} left.")
        if dogEnergy <= 0:
            passout("Doggo is too tired to walk and passes out.")
        else:
            entrance()

    elif "lawn" in choice:
        print("Your dog and you head over to the Big Lawn.\n...")
        bigLawn()

    elif "woods" in choice:
        print("Your dog and you head into Pine Woods.\n...")
        woods()

    elif "exit" in choice:
        print("You are leaving the Dog Park.")
        try:
            leave = input("Are you sure you want to leave? y or n?\n>")
            if leave == "y":
                print(f"Your dog has {dogEnergy} energy left. See you next time!")
                exit()
            elif leave == "n":
                entrance()
            else:
                print("I don't understand, please try again")
        except:
            print("Thanks for playing!")
    else:
        print("I don't undertstand, please try again")
def woods():
    global dogEnergy
    print("You are now in the Pine Woods. Here your dog can Chase Squirrels, Dig Holes, go to the Big Lawn, or head back to the Entrance.")
    choice = input(">")

    if "chase" in choice:
        chaseEnergy = 40
        print("Squirrels run in bushes and trees away from your dog. The chase goes on for awhile until there are no more squirrels in sight")
        dogEnergy = dogEnergy -chaseEnergy
        print(f"Your dog has {dogEnergy} left.")
        if dogEnergy <= 0:
            passout("Doggo is too tired to chase and passes out")
        else:
            woods()

    elif "dig" in choice:
        digEnergy = 30
        print("The soil here is soft enough to dig a deep hole in no time. Your dog digs hole after hole until he has had enough")
        dogEnergy = dogEnergy -digEnergy
        print(f"Your dog has {dogEnergy} left.")
        if dogEnergy <= 0:
            passout("Doggo is too tired to dig and passes out")
        else:
            woods()

    elif "lawn" in choice:
        print("Your dog and you head over to the Big Lawn.\n...")
        bigLawn()

    elif "Entrance" in choice:
        print("Your dog and you head back to the Entrance.\n...")
        entrance()

    else:
        print("I don't understand, please try again.")

def bigLawn():
    global dogEnergy
    print("You are now on the Big Lawn. Here you can play Fetch, let your dog run around with other dogs, go to the Pine Woods, or head back to the Entrance.")
    choice = input("> ")

    if "fetch" in choice:
        fetchEnergy = 50
        print("You throw your a ball as far ass you can and every time your dog brings is back. What a good boy!")
        dogEnergy = dogEnergy -fetchEnergy
        print(f"Your dog has {dogEnergy} left.")
        if dogEnergy <= 0:
            passout("Doggo is too tired to fetch and passes out")
        else:
            bigLawn()

    elif "run" in choice:
        runEnergy = 40
        print("Your dog runs around with a pack of other park dogs until you call him back to you.")
        dogEnergy = dogEnergy -runEnergy
        print(f"Your dog has {dogEnergy} left.")
        if dogEnergy <= 0:
            passout("Doggo is too tired to run and passes out.")
        else:
            bigLawn()

    elif "woods" in choice:
        print("Your dog and you head into Pine Woods.\n...")
        woods()

    elif "entrance" in choice:
        print("Your dog and you head back to the Entrance.\n...")
        entrance()

    else:
        print("I don't understand. please try again.")

def start():
    print('This program is game called "Dog Park". The objective of the game is to reduce your dogs energy with activities in the park.')
    print("If you decrease your dogs energy too much, he will pass out. Exit the park to end the game and see how well you did to decrease your dogs energy.")
    print("Press <Enter> to start the game")

    input("> ")

    entrance()

start()
