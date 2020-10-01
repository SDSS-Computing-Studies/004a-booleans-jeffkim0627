#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
number = float(input("Enter the number"))
value = number % 2
if value == 1:
    print("the number is odd")
else :
    print("The number is even")