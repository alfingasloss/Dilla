def main_menu():
    while True:
        print("Pilihan Program:")
        print("1. Read a character and display the corresponding name")
        print("2. Determine the quadrant of an angle")
        print("3. Number of days in a month")
        print("4. Determine the letter grade")
        print("5. Read marriage status code")
        print("6. Convert temperature")
        print("7. End program")
        
        # Minta input pilihan dari pengguna
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

        match pilihan:
            case '1':
                read_character()  # Memanggil fungsi untuk membaca karakter
            case '2':
                determine_quadrant()  # Memanggil fungsi untuk menentukan kuadran
            case '3':
                number_of_days()  # Memanggil fungsi untuk menentukan jumlah hari dalam bulan
            case '4':
                determine_letter_grade()  # Memanggil fungsi untuk menentukan nilai huruf
            case '5':
                read_marriage_status_code()  # Memanggil fungsi untuk membaca kode status pernikahan
            case '6':
                convert_temperature()  # Memanggil fungsi untuk mengonversi suhu
            case '7':
                end_program()  # Memanggil fungsi untuk mengakhiri program
                break
            case _:
                print("Invalid choice, please select 1, 2, 3, 4, 5, 6, or 7.")


def read_character():
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

        # Check if the user wants to quit
        if char_input.lower() == 'exit':
            print("Exiting the character reading function.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            break

        # Display the corresponding name or character based on the input
        print("The corresponding name is:", get_name_from_char(char_input))
        print('-------------------------------------------------------------')


def determine_quadrant():
    # Function to determine the quadrant based on the angle
    def get_quadrant(angle):
        if 0 <= angle < 90:
            return "Quadrant 1"
        elif 90 <= angle < 180:
            return "Quadrant 2"
        elif 180 <= angle < 270:
            return "Quadrant 3"
        elif 270 <= angle < 360:
            return "Quadrant 4"
        else:
            return "Invalid angle, must be between 0 and 360"

    # Loop to repeatedly ask for angle input
    while True:
        try:
            # Ask for angle input from the user
            angle_input = input("Enter an angle in degrees (or type 'exit' to quit): ")

            # Check if the user wants to exit
            if angle_input.lower() == 'exit':
                print("Exiting the quadrant determination function.")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            
            # Convert input to an integer
            angle = int(angle_input)
            
            # Determine the quadrant and display the result
            print(f"The angle {angle} is in {get_quadrant(angle)}")
            print('-------------------------------------------------------------')
        
        # Handle error if the input is not a valid number
        except ValueError:
            print("Invalid input, please enter a valid number or type 'exit' to quit.")
            print('-------------------------------------------------------------')


def number_of_days():
    # Function to determine the number of days based on the month name
    def get_number_of_days(month):
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
            print("Exiting the number of days function.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            break
        
        # Display the number of days in the entered month
        print(f"The month {get_number_of_days(month_input)}")  # Only display the result from the function
        print('-------------------------------------------------------------')


def determine_letter_grade():
    # Function to determine the letter grade
    def letter_grade(score):
        if score >= 90:
            return 'A'  # If score >= 90
        elif 80 <= score < 90:
            return 'B'  # If score is between 80 and 89
        elif 70 <= score < 80:
            return 'C'  # If score is between 70 and 79
        elif 60 <= score < 70:
            return 'D'  # If score is between 60 and 69
        else:
            return 'F'  # If score is below 60

    # Loop to repeatedly ask for input
    while True:
        try:
            # Ask for the score input from the user
            score_input = input("Enter the student's numerical score (or type 'exit' to quit): ")
            
            # Check if the user wants to exit
            if score_input.lower() == 'exit':
                print("Exiting the letter grade determination function.")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            
            # Convert input to float to support decimal numbers
            score = float(score_input)
            
            # Determine the letter grade and display the result
            print(f"The letter grade for the score {score} is {letter_grade(score)}")
            print('-------------------------------------------------------------')

        except ValueError:
            print("Invalid input, please enter a valid number or type 'exit' to quit.")
            print('-------------------------------------------------------------')


def read_marriage_status_code():
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
            print("Exiting the marriage status code function.")
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


def convert_temperature():
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
            print("Exiting the temperature conversion function.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            break
        
        else:
            print("Invalid choice, please choose 1, 2, or 3.")
            print('-------------------------------------------------------------')


def end_program():
    print("Program terminated. Thank You!")
    print('=============================================================')


if __name__ == "__main__":
    main_menu()
