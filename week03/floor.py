# floor.py
# Takes a float and outputs an integer rounded down
# Author: John Crumlish

import math
# Math is a built in module

number_to_floor = float(input("Enter a Float Number: "))
floored_number = math.floor(number_to_floor)
print('{} floored is {}' .format(number_to_floor, floored_number))