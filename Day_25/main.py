import random

print("⚔️⚔️ Character Generator ⚔️⚔️")
print()

def rollDice(sides):
  outcome = random.randint(1, sides)
  return outcome

def healthStat():
  sixSideOutcome = rollDice(6)
  eightSideOutcome = rollDice(8)
  health = sixSideOutcome * eightSideOutcome
  return health

while True:
  characterName = input("Name your legend?: ")
  health = healthStat()
  print(f"{characterName}'s health point is: {health}hp")
  print()
  newCharacter = input("Do you want to create another character?: ")
  if newCharacter.lower() == "yes":
    print()
    continue
  else:
    exit()
  