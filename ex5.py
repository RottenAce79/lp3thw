name = 'John Doe'
age = 43 # not a lie
height = 67 # inches
height_in_metric = height * 0.0254 # m
weight = 169
weight_in_metric = weight * 0.45359237 # kg
eyes = 'Hazel'
teeth = 'White'
hair = 'Black'

# f-strings do string interpolation
print(f"Let's talk about {name}.")
print(f"He's {height} inches or {height_in_metric} meters tall.")
print(f"He's {weight} pounds or {weight_in_metric} kilos heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
