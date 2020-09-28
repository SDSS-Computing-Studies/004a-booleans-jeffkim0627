#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
import math
number = float(input("Enter a number"))
value = math.ceil(number)
if number == value:
    print("The number is integer")
else :
    print("The number is not an integer")