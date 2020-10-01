#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
number = float(input("Enter the number"))
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
elif number < 0:
    print("The number is negative")