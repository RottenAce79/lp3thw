from sys import argv

print('''Script: {}
First argument: {}
Second argument: {}
Third argument: {}
Fourth argument: {}'''.format(*argv)) # argv is a list and * unpacks its items so that format() can use them
