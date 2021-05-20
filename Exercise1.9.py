def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party.")
    print("Get the booze.")

print("We can just give the function numbers")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside it too.")
cheese_and_crackers(10 + 10, 20 * 2)

print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers - 10)


