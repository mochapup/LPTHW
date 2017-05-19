# asking age
print("How old are you?", end= ' ')
age = input()
# asking height
print("How tall are you?", end=' ')
height = input()
# asking weight
print("How much do you weigh?", end=' ')
weight = input()

# print formatting sentence
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

def number_of_roaches(bugs):
    amount = bugs * 100
    print(f"If you see {bugs} roach, there are probably {amount} behind the walls")

bugs = float(input("How many roaches did you see?"))

number_of_roaches(bugs)
