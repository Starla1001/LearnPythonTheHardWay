
name = 'Philip Hill'
age = 44
height_cm = 180  # in centimetres
height_in = round(height_cm / 2.53)  # in inches
weight_kg = 74  # in kilograms
weight_lbs = round(weight_kg * 2.205)  # in pounds
eyes = "Green"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimetres or {height_in} inches tall.")
print(f"He's {weight_kg} kilos or {weight_lbs} pounds heavy.")
print("That's not too bad.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are normally {teeth} depending on the coffee.")

total = age + height_in + weight_lbs
total1 = age + height_cm + weight_kg

print(f"If you add your age: {age} and your height in inches {height_in} and your weight in pounds {weight_lbs}.")
print(f"You get {round(total)}.")
print(f"If you add your age: {age} and your height in centimetres {height_cm} and your weight in kilos {weight_kg}.")
print(f"You get {round(total1)}.")




