print("Loan Calculator 🧮🧮")
print()

loanAmount = 1000
apr = 0.05

for year in range(10):
  loanAmount += loanAmount * apr
  loanAmount = round(loanAmount, 2)
  print("Year", year+1, ": You owe $", loanAmount)
  print()