# read-count-file.py
# Reads in a number from a file that already exists
# Author: John Crumlish

FILENAME = "count.txt"
def read_number():
    with open (FILENAME) as f:
        number = int(f.read())
        return number

# Test it
num = read_number()
print(num)