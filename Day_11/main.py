print("How many seconds are in a year 🤔🤔? ")
print()
year = int(input("What year is it?: "))

secondsInAMinute = 60
minutesInAnHour = 60
hoursInADay = 24
daysInAYear = 365
daysInALeapYear = 366

if year % 4 == 0:
  secondsInAYear = secondsInAMinute * minutesInAnHour * hoursInADay * daysInALeapYear
  print("There are", secondsInAYear, "seconds in a leap year.")
else: 
  secondsInAYear = secondsInAMinute * minutesInAnHour * hoursInADay * daysInAYear
  print("There are", secondsInAYear, "seconds in a year.")