people = 30
cars = 30
trucks = 30

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We shouldn't take the cars.")
else:
    print("I can't decide")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we can take the trucks.")
else:
    print("Still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's go home.")
