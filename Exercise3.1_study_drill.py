# A simple text adventure based on series 1 episode 1 of Red Dwarf. "The End"

width = 20
print('Red Dwarf'.center(width, '-'))
print("The End".center(width, "-"))

print("""You are walking down a corridor pushing a service trolley accompanied by Arnold Rimmer.
You are currently singing a song as you go.
Rimmer ask you to shut up.

1: Do you stop singing and start humming.
2: Carry on singing ignoring him.
3: Be Quiet.""")

lister = input("> ")

if lister == "1":
    print("""You stop singing and start humming the theme tune from the Sound of music.
Rimmer spins around. 'Will you shut up!!!!'

1: Shut up.
2: start slapping your cheeks with your hands.
""")
elif lister == "2":
    print("""Rimmer spins around, 'SHUT UP.'
    
1: Shut up.
2: Start slapping your cheeks with your hands
""")

else:
    print("""You be quiet and follow him around the corner to a
broken down vending machine.""")

lister = input("> ")

if lister == "1":
    print("""You be quiet and follow him around the corner to a
broken down vending machine.""")

else:
    print("""Rimmer looks at you in total shock...
'That's it mi lado, Your on report'. Rimmer pulls out his 
notepad and scribbles something in it and replaces it to hit shirt pocket.
You stand in front of a knackered vending machine.""")

print("""O.k what job number is this Rimmer asks.

1: Stay quiet as he said, Blank him.
2: Tell him.""")

lister = input("> ")

if lister == "1":
    print("""You stay quiet....'Right that's it'. He pulls out the notepad and writes.
David Lister. Offence.....Singing, humming and being quiet.""")

elif lister == "2":
    print("That's better. A little bit of respect.")

print("""'Right..Job number 172. Chicken soup nozzle clogged.
Pass me a 14b lister.

1: Pass him a 14b
2: Pass him a 14c
""")

lister = input("> ")

if lister == "1" or "2":
    print("""You hand Rimmer a long white pipe cleaner. He looks at it in distain.
    "Does this look anything like a 14b.' He rummages around in the trolley
    and picks out an identical pipe cleaner and shows it to Lister.
    'This is a 14b, this is a 14f, are you blind. he replaces the 14b back in the trolley
    and uses the 14f to unblock the machine.""")

print("""Rimmer uses the pipe cleaner on the vending machine. 'Chicken soup please' he says
after cleaning the machine. The machine dispenses a milk white broth. Rimmer takes a sip
and spits it out on the floor. 'Yep, that's fine.""")






