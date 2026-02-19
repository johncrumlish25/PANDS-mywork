# isEven.py
# Will test if number is odd or even
# Author: John Crumlish

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print(f"{number} is an even number")
else: 
    print(f"{number} is an odd number")