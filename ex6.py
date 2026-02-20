types_of_people = 10
x = f"There are {types_of_people} types of people." # technically not putting in a string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # place one and two

print(x)
print(y)

print(f"I said: {x}") # place three
print(f"I also said: '{y}'") # place four

# not inverts a boolean value
hilarious = not False
joke_evaluation = "Isn't that joke so funny?! {}"

# .format() does what f-strings do except the initial string contains empty braces where the value goes and variable is put in .format() instead
print(joke_evaluation.format(hilarious)) # technically not putting in a string

w = "This is the left side of..."
e = "a string with a right side."

# strings can be added together; this is called string concatenation
print(w + e)
