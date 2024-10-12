# Program to convert temperature between Fahrenheit and Celsius

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return 5/9 * (fahrenheit - 32)  # Using the conversion formula

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32  # Using the conversion formula

# Looping to prompt the user for choices
while True:
    # Display choices to the user
    print("Choices:")
    print("1. Convert from Fahrenheit to Celsius")
    print("2. Convert from Celsius to Fahrenheit")
    print("3. Exit")
    
    # Prompt for user input
    choice = input("Enter your choice (1/2/3): ")
    
    # Check the user's choice
    if choice == '1':
        try:
            # Prompt for temperature in Fahrenheit
            fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
            # Convert and display the result
            celsius = fahrenheit_to_celsius(fahrenheit_input)
            print(f"{fahrenheit_input}°F is {celsius:.2f}°C")
            print('-------------------------------------------------------------')
        except ValueError:
            print("Invalid input, please enter a valid number.")
            print('-------------------------------------------------------------')
    
    elif choice == '2':
        try:
            # Prompt for temperature in Celsius
            celsius_input = float(input("Enter temperature in Celsius: "))
            # Convert and display the result
            fahrenheit = celsius_to_fahrenheit(celsius_input)
            print(f"{celsius_input}°C is {fahrenheit:.2f}°F")
            print('-------------------------------------------------------------')
        except ValueError:
            print("Invalid input, please enter a valid number.")
            print('-------------------------------------------------------------')
    
    elif choice == '3':
        print("Program terminated. Thank you!")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break
    
    else:
        print("Invalid choice, please choose 1, 2, or 3.")
        print('-------------------------------------------------------------')
