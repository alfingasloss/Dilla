# Program with a loop to read a character and display the corresponding name

# Function to get the name based on input character
def get_name_from_char(char):
    if char == 'F' or char == 'f':
        return 'Frank'
    elif char == 'C' or char == 'c':
        return 'Christine'
    elif char == 'A' or char == 'a':
        return 'Amanda'
    elif char == 'B' or char == 'b':
        return 'Bernard'
    else:
        return char

# Loop until the user decides to quit
while True:
    char_input = input("Enter a character (or type 'exit' to quit): ")

    # Check if the user wants to quit, whether 'exit' is typed in uppercase, lowercase, or mixed
    if char_input.lower() == 'exit':  # lower() ensures input is converted to lowercase
        print("Program terminated. Thank you!")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break

    # Display the corresponding name or character based on the input
    print("The corresponding name is:", get_name_from_char(char_input))
    print('=================================================')