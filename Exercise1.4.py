
from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like you to answer a few questions.")
print(f"Do you like me {user_name}?.")
like = input(prompt)

print(f"Where do you live {user_name}?.")
lives = input(prompt)

print("What type of computer do you have?.")
computer = input(prompt)

print(f"""
Alright {user_name}, so you said {like} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")