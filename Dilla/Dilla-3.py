# Program to display the number of days in a month

# Function to determine the number of days based on the month name
def number_of_days(month):
    # Convert the input month to lowercase for easier checking
    month = month.lower()
    
    # List of months with 31 days (in lowercase)
    months_31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
    # List of months with 30 days (in lowercase)
    months_30 = ['april', 'june', 'september', 'november']
    
    # If the month is in the list of 31 days
    if month in months_31:
        return f"{month.capitalize()} has 31 days."
    # If the month is in the list of 30 days
    elif month in months_30:
        return f"{month.capitalize()} has 30 days."
    # If the month is February
    elif month == 'february':
        return "February has 28 or 29 days (leap year)."
    # If the input month is invalid
    else:
        return f"'{month.capitalize()}' is not valid, please enter a correct month name."

# Loop to repeatedly ask for input
while True:
    # Ask for month input from the user
    month_input = input("Enter the name of the month (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if month_input.lower() == 'exit':  # Convert input to lowercase to check for 'exit'
        print("Program terminated. Thank you!")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break
    
    # Display the number of days in the entered month
    print(f"The month {number_of_days(month_input)}")  # Only display the result from the function
    print('-------------------------------------------------------------')
