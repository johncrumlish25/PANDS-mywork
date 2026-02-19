# garde.py
# Reads in a student’s percentage mark and prints out corresponding grade
# Author: John Crumlish

percentage = float(input("Enter the percentage: "))

# Acts as an error message
if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")

elif percentage < 40:  # Less than 40
    print("Fail")
elif percentage < 50:  # Between 40 and 49
    print("Pass")
elif percentage < 60:  # Between 50 and 59
    print("Merit1")
elif percentage < 70:  # Between 60 and 69
    print("Merit2")
else:                  # Above 70
    print("Distinction")