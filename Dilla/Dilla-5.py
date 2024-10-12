# Program to read marriage status code and display the corresponding message

# Function to determine the message based on the status code
def marriage_status(code):
    if code.lower() == 'm':
        return "Individual is married."  # Message for married status
    elif code.lower() == 'd':
        return "Individual is divorced."  # Message for divorced status
    elif code.lower() == 'w':
        return "Individual is a widower/widow."  # Message for widower/widow status
    else:
        return "Invalid code entered."  # Message for invalid code

# Loop to repeatedly ask for input
while True:
    # Ask for input from the user
    code_input = input("Enter the marriage status code (M/m, D/d, W/w) or type 'exit' to quit: ")
    
    # Check if the user wants to exit
    if code_input.lower() == 'exit':
        print("Program terminated. Thank you!")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break
    
    # Ensure input is only one character
    if len(code_input) != 1:
        print("Please enter only one character for the status code.")
        print('-------------------------------------------------------------')
        continue
    
    # Display the message based on the status code
    print(marriage_status(code_input))
    print('-------------------------------------------------------------')
