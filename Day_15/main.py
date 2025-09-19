print("Animal sounds 🐮🐶🐴🐔🐷")

exit = ""
while exit != "yes":
  print()
  animal = input("What animal do you want to hear?: ")
  animal = animal.lower()
  
  if animal == "cow":
    print("A cow goes moooooooo... 🐮")
  elif animal == "dog":
    print("A dog goes woof woof 🐶")
  elif animal == "horse":
    print("A horse goes neigh... 🐴")
  elif animal == "chicken":
    print("A chicken goes cluck cluck 🐔")
  elif animal == "pig":
    print("A pig goes oink oink 🐷")
  else:
    print("This animal is not available for now, please check back later.")
  
  print()
  exit = input("Do you want to exit?: ")
  exit = exit.lower()