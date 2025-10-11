from getpass import getpass as input

print("Epic 🪨| 📄| ✂️ battle 🔥🔥")
print()
print("Please use 'R' for rock, 'P' for paper, and 'S' for scissors.")

player1Score = 0
player2Score = 0

round = 1

while True:
  if player1Score == 3:
    print()
    print("Congratulations player 1, you won 🥳🥳🥳")
    exit()
  elif player2Score == 3:
    print()
    print("Congratulations player 2, you won 🥳🥳🥳")
    exit()
  else:
    print()
    print("Round", round, "🔥🔥")
    print()
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")
    
    if player1 == "R" or player1 == "r":
      if player2 == "S" or player2 == "s":
        print("Rock smashes scissors. Player 1 wins 🔥🔥")
        player1Score += 1
        round += 1
      elif player2 == "P" or player2 == "p":
        print("Paper smothers rock to nothingness. Player 2 wins 🔥🔥")
        player2Score += 1
        round += 1
      elif player2 == "R" or player2 == "r":
        print("Rock and Rock cancels each other. WE HAVE A DRAW 🔥🔥")
        round += 1
      else:
        print("Player 2 please use 'R' for rock, 'P' for paper, and 'S' for scissors.")
    
    elif player1 == "P" or player1 == "p":
      if player2 == "R" or player2 == "r":
        print("Paper folds up rock. Player 1 wins 🔥🔥")
        player1Score += 1
        round += 1
      elif player2 == "S" or player2 == "s":
        print("Scissors cuts up paper. Player 2 wins 🔥🔥")
        player2Score += 1
        round += 1
      elif player2 == "P" or player2 == "p":
        print("Paper and Paper. WE HAVE A DRAW 🔥🔥")
        round += 1
      else:
        print("Player 2 please use 'R' for rock, 'P' for paper, and 'S' for scissors.")
    
    elif player1 == "S" or player1 == "s":
      if player2 == "R" or player2 == "r":
        print("Rock smashes scissors. Player 2 wins 🔥🔥")
        player2Score += 1
        round += 1
      elif player2 == "P" or player2 == "p":
        print("Scissors cuts up paper mercilessly. Player 1 wins 🔥🔥")
        player1Score += 1
        round += 1
      elif player2 == "S" or player2 == "s":
        print("Scissors and Scissors. WE HAVE A DRAW 🔥🔥")
        round += 1
      else:
        print("Player 2 please use 'R' for rock, 'P' for paper, and 'S' for scissors.")
    
    else:
      print("Player 1 please use 'R' for rock, 'P' for paper, and 'S' for scissors.")
    
    print("Player 1 (", player1Score,") -", "Player 2 (", player2Score,")")