#Importing arguments
from sys import argv

# arguments
script, filename = argv

# opening the file
txt = open(filename)

# printing the filename and contents
print(f"Here's your file {filename}:")
print(txt.read())

# input request for filename
#print("Type the filename again:")
file_again = input("> ")

# assigning input to file
#txt_again = open(file_again)

#printing file contents agian
#print(txt_again.read())
