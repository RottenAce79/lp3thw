'''
#import 'arguments provided in command line' feature from 'system' library
from sys import argv

#unpack arguments provided in command line
script, filename = argv
'''

#open a file and store it as a variable
filename = input('enter name of the file you want to print: ') #input() method is maybe less verbose but more annoying to use from user's perspective
txt = open(filename)

#read and print the file stored in the variable
print(f"Here's your file {filename}:")
print(txt.read())

txt.close() #files should be closed properly after openning them

'''
#ask for another file
print("Type the filename again:")
file_again = input("> ")

#open the newly provided file and store it in a variable
txt_again = open(file_again)

#read and print the newly provided file
print(txt_again.read())

txt_again.close()
'''
