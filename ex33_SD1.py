# ex33.py
# Exercise 33: While Loops

# Defining variables and creating numbers list

def main():
    i = 0
    numbers = []
    var1 = 6
    while i < var1:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")
    for num in numbers:
        print(num)

main()
