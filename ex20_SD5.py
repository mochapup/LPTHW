# Functions and files
# import argv
from sys import argv
# Scripr and argument input
script, input_file = argv
#  defining function that prints all of file
def print_all(f):
    print(f.read())
# defining a function to rewind to character 0 of file
def rewind(f):
    f.seek(0)
# defining a function to print each line seperately with its line count.
def print_a_line(line_count, f):
    print(line_count, f.readline())
# opening argument file
current_file = open(input_file)
# reading and printing the argument file
print("First let's print the whole file:\n")
print_all(current_file)
# Moving to line 0 of the file
print("Now let's rewind, kind of like tape.")
rewind(current_file)
# Printing each line starting with line one
print("Let's print three lines:")
# defining current line, in argument file, and adding itself 1 each succesion.
#Then running the print_a_line function with current_line.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
