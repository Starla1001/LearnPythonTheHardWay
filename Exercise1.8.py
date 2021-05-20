# Names, Variables, Code, Functions

# this one is like the scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that args is pointless, Like this.

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes 0 arguments

def print_none():
    print("I got nothing!!!")

print_two("Philip", "Hill")
print_two_again("Philip", "Hill")
print_one("First")
print_none()