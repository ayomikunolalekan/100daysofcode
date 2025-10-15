print("Basic Login System 🪪🪪")
print()

username = "Ayomikun"
userPassword = "programmers4life"

def login():
  while True:
    name = input("What is your username?: ")
    if name == username:
      password = input("What is your password?: ")
      
      if password == userPassword:
        print()
        print("Welcome to Basic,", username, "😁😁")
        exit()
      else:
        print("Your password is incorrect, please try again!!")

    else:
      print("Your username is incorrect, please try again!!")

    print()


login()
