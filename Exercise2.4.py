print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explination
\n\t\twhere there is none.
"""
print("__________________")
print(poem)
print("__________________")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
bean, jars, creates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# It's just like with a f"" string
print(f"We'd have {bean} beans, {jars} jars and {creates} crates.")

start_point = start_point / 10

print("We can also do it this way:")
formula = secret_formula(start_point)






