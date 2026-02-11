# div.py
# This program will divide numbers
# Author: John Crumlish

x = int(input("Enter First Number: "))
y = int(input("Enter Number You Want To Divide By: "))
answer = int(x//y) #// divides
remainder = x%y    #% gives remainder

print("{} divided by {} is {} with remainder {}" .format(x, y, answer, remainder))

#answer will say 3 is 3 which means 3.3