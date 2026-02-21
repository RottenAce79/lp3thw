def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#sd3
def print_arg(arg):
    print(f"value of arg: {arg}")

print_arg("lool")
print_arg(123)
print_arg(True)
print_arg("top" + ' ' + "zozzle")
print_arg(True * False)
print_arg("ayy" + "lmao")
print_arg(input("enter something: "))
print_arg(print("huh"))
print_arg(repr(cheese_and_crackers))
print_arg('e' * 14)
