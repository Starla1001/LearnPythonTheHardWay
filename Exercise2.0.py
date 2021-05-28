# from the system library import the argv module.
from sys import argv
# set up the arguments for argv
script, input_file = argv

# functions
def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

# Creates a variable "current_file"
current_file = open(input_file)
# Prints
print("First lets print the whole file.\n")
# Calls the function "print_all"
print_all(current_file)
# Prints
print("Now let's rewind, kind of like a tape.")
# Calls the function "rewind"
rewind(current_file)
# Prints
print("Let's print 3 lines:")
# Calls function "print_a_line" from line 1 then add 1 to 2 etc.......
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
