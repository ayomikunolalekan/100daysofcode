print("Color Subroutine 🎨🎨")

def colorCodes(color, word):
  if color == "blue":
    print("\033[0;34m", word, sep="", end="")
  elif color == "orange":
    print("\033[38;5;208m", word, sep="", end="")
  elif color == "green":
    print("\033[0;32m", word, sep="", end="")
  elif color == "default":
    print("\033[0m", word, sep="", end="")


print()
print("The sun rose slowly over the calm ", end="") 
colorCodes("blue", "blue ocean, painting the sky with gentle strokes of ") 
colorCodes("orange", "orange and pink. Nearby, the ") 
colorCodes("green", "green palm trees swayed gracefully, ")
colorCodes("default", "welcoming a brand-new day filled with peace and promise.")

