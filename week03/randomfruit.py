# randomfruit.py
# This program will generate a random fruit
# Author: John Crumlish

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print ("A Random Fruit: {}" .format(fruit))

# () is a tuple
# [] is a list