print("Fill in the blank lyrics 🎵🎵")
print()

counter = 0

while True:
  print("I've got two tickets to Iron ______, baby. Come with me Friday don't say maybe")
  lyric = input("What's the missing word?: ")
  counter += 1
  if lyric == "maiden" or lyric == "Maiden":
    break
  else:
    print("That's wrong ❌, try again !!")
    print()

print()
print("Nice 🥳🥳 you got it in", counter, "tries")