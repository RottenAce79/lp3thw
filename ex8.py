formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
#replace space character with newline character in formatter string using replace() function and feed its output to format() function
print(formatter.replace(' ', '\n').format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

'''
print(formatter.format(
    "Try your\n", # \n is a newline character in source code
    "Own text here\n", # instead of text being concatinated on the same line
    "Maybe a poem\n", # each string is printed on a new line instead
    "Or a song about fear"
))
'''
