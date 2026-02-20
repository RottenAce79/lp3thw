#variable definitions
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#variable definitions based on existing variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


#values of variables are put into print command inbetween text
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#sd0 error means that variable with that name is not defined - root cause is a typo
#sd1 not necessary because the free space in a car is a whole number; if a whole number is used result in carpool_capacity will also be a whole number
#sd4 = symbol is used for assignment; in context of this exercise = assigns value to its right to the label to its left
