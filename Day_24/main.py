import random

print("Infinity Dice 🎲🎲")
print()
print("Instruction: When asked if you want to roll the dice again, please only answer with yes or no. Thank you 🙏🏽")
print()

def rollDice(sides):
  result = random.randint(1,sides)
  print("You rolled", result)


numberOfSides = int(input("How many sides should your dice have?: "))

while True:  
  rollDice(numberOfSides)
  print()
  anotherRoll = input("Do you want to roll again?: ")
  if anotherRoll.lower() == "yes":
    continue
  else:
    exit()