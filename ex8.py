# Defining formatter
formatter = "{} {} {} {}"

#Printing formats
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Line one of a song",
"Line two of a song",
"A short poem I guess",
"A final line of text"
))

# Mistake: I only aded one parenthacese instead of two at the end of line 8
# doing thing was showing an error on line 9, so I was a bit confused at first
