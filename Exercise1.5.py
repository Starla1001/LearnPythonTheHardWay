
from sys import argv
# Asks to enter your script name and text file you want to use
script, filename = argv
# Creates the handle "txt" and opens the text file entered as filename
txt = open(filename)
# prints "Here is your file Exercise1.5.txt
print(f"Here is your file {filename}:")
# prints the text in the file
print(txt.read())
txt.close()


# asks to type the file name again
#print("Type the filename again:")
#file_again = input("> ")
# Creates the handle txt_again and opens the file
#txt_again = open(file_again)
# prints text file again
#print(txt_again.read())
