print("30 Days of Code Review 🥳🥳")
print()
print("In one word describe how each of the 30 days of code has been for you.")
print()

for day in range(1,31):
  print(f"Day {day}:")
  response = input()
  review = f"You thought day {day} was {response}"
  print()
  print(f"{review: ^35}\n")