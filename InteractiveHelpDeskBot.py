# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support").
#  If a command is found, print a response related to the command.

def commandParser(userInput):
    preCommands = ["help", "issue", "contact support"]
   
    for command in preCommands:
        if command in userInput:
            if command == "help":
                print("It seems you need help. please check our FAQs before contacting Support.")
            elif command == "issue":
                print('It seems you have an issue')
            elif command == "contact support":
                print("For support, contact us at support@codingtemple.com")
            return

    print("Not a valid command please try again")

userInput = input('How can I assist you today? ("help", "issue", "contact support") if "issue" please explain ("login", "performance", "error", etc.")')


# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. 
# Print out the category of the issue for the support team.
def issue(userInput):
    if "login" in userInput:
        print("Issue: Login ")
    elif "performance" in userInput:
        print("Issue: Performance ")
    elif "error" in userInput:
        print("Issue: Error")
    elif "other" in userInput:
        print("Issue: Other")
    else:
        print("No specific issue mentioned.")
issue(userInput)
commandParser(userInput)