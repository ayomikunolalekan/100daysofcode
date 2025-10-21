import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()
  
pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    stopPlayback = int(input("Select 2 anytime to pause playback and go back to the menu: "))
    if stopPlayback == 2:
      pause()
      return  # let's go back from this play() subroutine
    else:
      continue


while True:
  # clear the screen 
  os.system("cls")

  # Show the menu
  print("Music Player 🎶🎶")
  time.sleep(1)

  print()
  print("MENU")
  print("------------------")
  time.sleep(1)

  print("Select 1 to play")
  print("Select 2 to exit")
  print()
  print("Select any other number to see the menu again.")
  time.sleep(1)

  # take user's input
  userChoice = int(input("Select an Option: "))

  # check whether you should call the play() subroutine depending on user's input
  if userChoice == 1:
    print("Jamming 🕺🏽🕺🏽")
    play()
  elif userChoice == 2:
    print("Goodbye")
    exit()
  else:
    userChoice = str(userChoice)
    continue