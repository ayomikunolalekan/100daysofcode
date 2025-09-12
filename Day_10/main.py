print("Bill Calculator 🧮")
print()
billAmount = float(input("What was the total bill?: "))
tipPercentage = int(input("What percentage do you want to tip?: "))
numberOfIndividuals = int(input("How many people?: "))

tipAmount = (tipPercentage / 100) * billAmount
finalAmount = (tipAmount + billAmount) / numberOfIndividuals
finalAmount = round(finalAmount, 2)

if numberOfIndividuals == 1:
  print("You owe: $", finalAmount)
elif numberOfIndividuals == 2:
  print("You both owe: $", finalAmount)
elif numberOfIndividuals > 2:
  print("You all owe: $", finalAmount)