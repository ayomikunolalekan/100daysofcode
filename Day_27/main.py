import os, time, random

# colors
default = "\033[0m"
green = "\033[32m"
red = "\033[31m"

# Character subroutine
def character():
  warrior = input("Name your warrior?: ")
  print()
  species = input("What type of creature (e.g human, elf, orc e.t.c) is your warrior?: ")
  return warrior, species

# dice subroutine
def rollDice(sides):
  outcome = random.randint(1, sides)
  return outcome

# health subroutine
def healthStat():
  sixSidedRoll = rollDice(6)
  twelveSidedRoll = rollDice(12)
  health = ((sixSidedRoll * twelveSidedRoll) // 2) + 10
  return health

# strength subroutine
def strengthStat():
  sixSidedRoll = rollDice(6)
  twelveSidedRoll = rollDice(12)
  strength = ((sixSidedRoll * twelveSidedRoll) // 2) + 12
  return strength


while True:
  os.system("cls")
  print("⚔️⚔️ Character Generator ⚔️⚔️")
  time.sleep(1)
  print()

  warriorName, warriorSpecie = character()
  health = healthStat()
  strength = strengthStat()
  time.sleep(1)
  print()

  print(warriorName, "the", warriorSpecie)
  print(f"{red}HEALTH: {health} {default}")
  print(f"{green}STRENGTH: {strength} {default}")
  time.sleep(1)
  print()

  print("May your luck in battle be neverending 🫡🫡")
  print()
  anotherCharacter = input("Would you like to create another warrior? Y for yes and N for no?: ")
  if anotherCharacter.lower() == "y":
    continue
  else:
    exit()