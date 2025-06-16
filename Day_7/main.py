print("Fake Fan Question Generator 👮👮")
print("+++++++++++++++++++++++++++++++++++")
print()

favoriteShow = input("What is your favoirte tv show/cartoon/anime?: ")
if favoriteShow == "Bleach":
  print("ooh a bleach fan, nice to meet you. If you are a bleach fan you should be able to answer this question")
  print()
  military = input("What is the name of the soul society  secret organization?: ")
  if military == "Gotei 13":
    print("Ding ding ding. You're absolutely correct. I can now vouch that you are not a fake fan 😅😅")
  else:
    print("OOF, I'm so sorry, you got it wrong but don't feel bad, even some real fans forget or make mistakes.")

elif favoriteShow == "Attack on titan":
  print("Ah AOT 😭😭. Good choice my friend. Quick question just to confirm something")
  print()
  wall = input("What is the name of the outermost wall protecting humanity?: ")
  if wall == "Wall Maria" or wall == "Maria":
    print("Beautiful Wall Maria, you're absolutely correct my friend. You're not a fake fan 😅😅 ")
  else:
    print("Sorry my friend, you're wrong. Should I call you a fake fan now or what 🤔😅")

else:
  print("Apologies brother or sister man, I was too lazy to create scenarios for other shows so I might have heard of it but I have to say I have never heard of that show 🥲")

