#  Exercise 24: More Practice
# practice printing and escapes
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# writing a multiline poem with escapes to variable poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# printing poem
print("--------------")
print(poem)
print("--------------")

# writing math sequence to variable
five = 10 - 2 + 3 - 6
# printing format string with variable
print(f"This should be five: {five}")

# writing function that returns value to variable
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# defining start point
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# its just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# redefining start point
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
