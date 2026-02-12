# normalise.py
# puts string in lower case and outputs its length
# Author: John Crumlish

raw_string = input("Enter a String: ")
normalised_string = raw_string.strip().lower()

length_raw_string = len(raw_string)
length_normalised_string = len(normalised_string)

print(f'That string normalised is: {normalised_string}')
print(f'we reduced the input string from {length_raw_string} to {length_normalised_string} characters')