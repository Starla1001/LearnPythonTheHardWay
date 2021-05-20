
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format (True, True, False, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Mary had a little lamb, ",
    "Her father shot it dead, ",
    "And now it goes to school with her, ",
    "Between two chunks of bread."
))
