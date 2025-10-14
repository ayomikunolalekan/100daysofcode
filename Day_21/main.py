print("Math Facts(Multiplication) 🧮🧮")
print()

multiple = int(input("Let's sharpen those math skills! What number should I quiz you on today?: "))
score = 0
print()

for num in range(1, 13):
  product = num * multiple
  print(num, "x", multiple)
  userResponse = int(input("Answer: "))
  if userResponse == product:
    print("Correct, Good job 🥳🥳")
    score += 1
  else:
    print("Wrong 😔. The answer is", product)

  print()

if score == 12:
  print("Wow! A perfect score! 🥳")
else:
  print("Awesome! You got", score, "points out of 12 🎯")