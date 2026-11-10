#User Name Generator

# first = input("Enter your first name: ").strip()
# last = input("Enter your last name: ").strip()

# username = (first[0] + last).lower()

# print(username)

#Number Guessing

# import random

# secret = random.randint(1, 10)
# guess = int(input("Guess a number between 1 and 10: "))

# if guess == secret:
#     print("Correct!")
# else:
#     print(f"Wrong. It was {secret}.")
fruits = ["Apple, Orange, Mango"] 

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):   # index and value together
    print(i, fruit)