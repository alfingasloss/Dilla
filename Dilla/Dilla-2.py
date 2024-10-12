# Program to determine the quadrant of an input angle

# Function to determine the quadrant based on the angle
def determine_quadrant(angle):
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
        print('-------------------------------------------------------------')

# Loop to repeatedly ask for input
while True:
    try:
        # Ask for angle input from the user
        angle_input = input("Enter an angle in degrees (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if angle_input.lower() == 'exit':
            print("Program terminated. Thank you!")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            break
        
        # Convert input to an integer
        angle = int(angle_input)
        
        # Determine the quadrant and display the result
        print(f"The angle {angle} is in {determine_quadrant(angle)}")
        print('-------------------------------------------------------------')
    
    # Handle error if the input is not a valid number
    except ValueError:
        print("Invalid input, please enter a valid number or type 'exit' to quit.")
        print('-------------------------------------------------------------')
