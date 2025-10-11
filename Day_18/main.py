print("Guess My Number 🔢🔢🤔")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")
print()

secretNumber = 570500
count = 1

while True:
  guess = int(input("What is your guess?: "))
  if guess == secretNumber:
    print("Correct 🥳🥳, you have successfully guessed my number")
    break
  elif guess >= 0 and guess < secretNumber:
    print("Your guess is too low 😔😔, Try again !!")
  elif guess > secretNumber:
    print("Your guess is too high 😔😔, Try again !!")
  else:
    print("Goodbye")
    exit()

  count += 1
  print()

print()
print("You guessed my number correctly in", count, "attempts. Well done 👏👏")