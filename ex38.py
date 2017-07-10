# ex38.py
# Exercise 38: Doing Things to Lists

# Creating a variable with string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# printing string
print("Wait there are not 10 things in that list. Let's fix that.")

# Spliting then_things variable and packing into 'stuff' as a Lists
stuff = ten_things.split(' ')
# creating more_stuff list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while loop that ends when 10 items are counted in 'stuff'
while len(stuff) != 10:
    # pops an item out of more stuff and is set to next_one
    next_one = more_stuff.pop()
    # prints what is being added from 'more_stuff' to 'stuff'
    print("Adding: ", next_one)
    # appending 'stuff' with 'next_one'
    stuff.append(next_one)
    # prints how many items are in 'stuff' now
    print(f"There are { len(stuff) } items now.")

# prints all items in stuff once loop is finished
print("There we go: ", stuff)

# prints item at index [1] in list
print(stuff[1])
# prints last item in list
print(stuff[-1]) # whoa! fancy
# pops item from list, default item is last item in list
print(stuff.pop())
# joins all items in list with space  between items
print(' '.join(stuff)) #what? cool!
# joins items indexed in range, sets a # between them.
print('#'.join(stuff[3:5]))
