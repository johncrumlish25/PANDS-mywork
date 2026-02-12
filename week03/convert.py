# convert.py
# Takes a float amount of dollars and returns that absolute amount in cents
# Author: John Crumlish

dollars = float(input("Enter Dollar Amount: "))
absolute_dollars = abs(dollars)
cents = int(absolute_dollars * 100)

print(cents)