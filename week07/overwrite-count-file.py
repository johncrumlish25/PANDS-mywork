# overwrite-count-file.py
# Takes in a number and overwrites a file with that number
# Author: John Crumlish

FILENAME = "count.txt"
def write_number(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number)) # write takes a string so need to convert

# Test it
write_number(3)