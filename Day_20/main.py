print("List Generator 📃📃")
print()

startingNumber = int(input("What number should your list start at?: "))
endingNumber = int(input("What number should your list end at?: "))
increment = int(input("Your list should be incremented or decremented by what number?: "))

if endingNumber > startingNumber:
  for num in range(startingNumber, endingNumber+1, increment):
    print(num)
elif endingNumber < startingNumber:
  for num in range(startingNumber, endingNumber-1, -(increment)):
    print(num)
else:
  print("Your list can't be generated as your starting value and ending value are the same.")