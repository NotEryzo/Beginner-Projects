"""
This is a code-along tutorial and is not my own work.
All credit goes to Bro Code.

"""

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Remove any '-' or ' '.
card_number = input("Enter a credit card number: ").strip()
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Add all digits in the odd places from right to left.
for i in card_number[::2]:
  sum_odd_digits += int(i)

# Double every second digit from right to left.
# If the result is a two-digit number, add the two-digit number together to get a single digit.

# How the math works.
# The largest that i can be is 18, because the largest a single digit can be is 9 in a credit card number.
# 9 * 2 is 18, 18 % 10 = 8 and we add 1 to get 9.

for i in card_number[1::2]:
  i = int(i) * 2
  if i >= 10:
    sum_even_digits += ((i % 10) + 1)
  else:
    sum_even_digits += i

# Sum the total.
total = sum_odd_digits + sum_even_digits

# If the sum is divisible by 10, then the credit card is valid.
if total % 10 == 0:
  print("Valid")
else:
  print("Invalid")
