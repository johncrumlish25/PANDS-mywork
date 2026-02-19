# average.py
# Keeps reading numbers until the user enters a 0
# Author: John Crumlish

numbers = []

number = int(input("Enter Number (0 to Quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("Enter Another (0 to Quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print (f"The Average is {average}")
