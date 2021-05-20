
# Creates a variable called cars and put the integer 100 in it.
cars = 100
# Creates a variable called space_in_car and puts the float 4.0 in.
space_in_car = 4
# Creates a variable called drivers and puts the integer 30 in.
drivers = 30
# Creates the variable passengers and puts 90 in it.
passengers = 90
# Creates a variable cars_not_driven by subtracting drivers from cars (100 - 90).
cars_not_driven = cars - drivers
# Creates a variable cars_driven which is equal to amount of drivers.
cars_driven = drivers
# Creates a variable carpool_capacity using cars_driven * space_in_car.
carpool_capacity = cars_driven * space_in_car
# Creates a variable average_passengers_per_car by dividing passengers by cars_driven.
average_passengers_per_car = passengers / cars_driven

# Using strings and variables to print the information.

print("there are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
