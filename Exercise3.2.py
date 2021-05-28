the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots', 'cherries']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit type: {fruit}")

# Going thru mixed lists

for i in change:
    print(f"i got {i}")

# Using the range function

elements = []

for i in range(0,10):
    print(f"adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}.")

