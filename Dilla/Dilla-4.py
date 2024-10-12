# Program to determine the letter grade based on a student's numerical score

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
            print("Program terminated. Thank you!")
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
