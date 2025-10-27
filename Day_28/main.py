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

# battle subroutine
def sixSideRoll ():
  outcome1 = rollDice(6)
  outcome2 = rollDice(6)
  return outcome1, outcome2


print("⚔️⚔️ Death Battle ⚔️⚔️")
time.sleep(1)
print()

warrior1, warrior1Specie = character()
warrior1health = healthStat()
warrior1strength = strengthStat()
time.sleep(1)
print()

print(warrior1, "the", warrior1Specie)
print(f"{red}HEALTH: {warrior1health} {default}")
print(f"{green}STRENGTH: {warrior1strength} {default}")
time.sleep(1)
print()

print("May your luck in battle be neverending 🫡🫡")
print()
print("Their Opponent?")
time.sleep(1)
print()

warrior2, warrior2Specie = character()
warrior2health = healthStat()
warrior2strength = strengthStat()
time.sleep(1)
print()

print(warrior2, "the", warrior2Specie)
print(f"{red}HEALTH: {warrior2health} {default}")
print(f"{green}STRENGTH: {warrior2strength} {default}")
time.sleep(1)
print()

print("May your luck in battle be neverending 🫡🫡")
time.sleep(1)

round = 1

while True:
  os.system("cls")
  print("⚔️⚔️ Death Battle ⚔️⚔️")
  time.sleep(2)
  print()

  print("Round", round)
  warrior1Roll, warrior2Roll = sixSideRoll()
  time.sleep(2)
  print()
  
  if warrior1strength > warrior2strength:
    damage = (warrior1strength - warrior2strength) + 1
  else:
    damage = (warrior2strength - warrior1strength) + 1
  
  if warrior1Roll > warrior2Roll:
    warrior2health -= damage
    print(warrior1, "wins round", round, "🔥🔥")
    print(warrior2, "gets hit and takes", damage, "damage")
    
  elif warrior2Roll > warrior1Roll:
    warrior1health -= damage
    print(warrior2, "wins round", round, "🔥🔥")
    print(warrior1, "takes a hit and suffers", damage, "damage")

  else:
    print("We have a tie 🔥🔥")
  time.sleep(2)
  
  print()
  print(warrior1, "the", warrior1Specie)
  print(f"{red}HEALTH: {warrior1health} {default}")
  print()

  print(warrior2, "the", warrior2Specie)
  print(f"{red}HEALTH: {warrior2health} {default}")

  time.sleep(2)
  print()
  
  if warrior1health < 1:
    print(warrior1, "has courageously died in battle 😔😔")
    print(warrior2, "is the winner 🫡🫡 and defeated", warrior1, "in", round, "round(s)")
    exit()

  elif warrior2health < 1:
    print(warrior2, "has courageously died in battle 😔😔")
    print(warrior1, "is the winner 🔥🔥 and defeated", warrior2, "in", round, "round(s)")
    exit()

  round += 1
  print()
  print("The battle continues ⚔️⚔️")
  time.sleep(2)