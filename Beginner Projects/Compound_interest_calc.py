"""
This is a code-along tutorial and is not my own work, but does contain very little modification.
All credit goes to Bro Code.

"""

principle = 0
rate = 0
time = 0

# Modified the code so that when the user enters somthing other than a number, it will ask the user to enter a valid input.
while principle <= 0:
  try:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
      print("Principle cannot be less than or equal to zero.")
  except:
    print("Please enter a number.")

while rate <= 0:
  try:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
      print("Interest rate cannot be less than or equal to zero.")
  except:
    print("Please enter a number.")

while time <= 0:
  try:
    time = int(input("Enter the time in years: "))
    if time <= 0:
      print("Time cannot be less than or equal to zero.")
  except:
    ("Please enter a number.")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s: ${total:,.2f}")  # Will add a comma to reperesent thousands, millions, etc.
