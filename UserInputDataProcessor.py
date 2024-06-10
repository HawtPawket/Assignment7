
# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

if len(firstName) < 2 or len(lastName) < 2:
    print("Whoops! First and last name should be at least 2 characters long.")

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, 
# and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

def passwordComplexity(password):
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        print("Password should contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        print("Password should contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        print("Password should contain at least one number.")

password = input("Enter your password: ")
passwordComplexity(password)

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format

def formatEmail(email):
    email = email.lower().strip()
    return email

userEmail = input("Enter your email address: ")
formattedEmail = formatEmail(userEmail)
print(f"Email address: {formattedEmail}")
