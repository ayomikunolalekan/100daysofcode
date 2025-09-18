print("Gradebook 📕📕")
print()
course = input("What course or subject were your exams on?: ")
maxScore = int(input("What is the maximum number of points you could have gotten on the test?: "))
userScore = float(input("What is your score on the test?: "))

scorePercentage = (userScore / maxScore) * 100
scorePercentage = round(scorePercentage, 2)
print("Based on your score, your total percentage is", scorePercentage, "%")

if scorePercentage >= 90 and scorePercentage <= 100:
  print("Congratulations 🥳🥳🥳, you got an A+ on your", course, "test. I'm really proud of you.")
elif scorePercentage >= 80 and scorePercentage <= 89:
  print("You got an A on your", course, " test, congratulations 🥳🥳🥳")
elif scorePercentage >= 70 and scorePercentage <= 79:
  print("You got a B on your", course, " test, congratulations my friend, you did good 🥳🥳🥳")
elif scorePercentage >= 60 and scorePercentage <= 69:
  print("You got a C on your", course, " test, you did good, I'm happy for you 🥳")
elif scorePercentage >= 50 and scorePercentage <= 59:
  print("You got a D on your", course, " test 🥲, you tried but you could have done better my friend")
else:
  print("You got a U on your", course, " test, I believe that is an ungraded. I'm really my friend, better luck next time.")
