#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks
username = input("Enter your name")
if username == "admin":
    password = input("Enter password")
    if password == "12345password":
        print("Access granted")
    else :
        print("Invalid password")
else :
    print("Invalid user")