# Program dengan menu utama yang menggabungkan berbagai fungsi

# Fungsi untuk mendapatkan nama berdasarkan karakter input
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
        return char  # Jika karakter tidak dikenali, kembalikan karakter itu sendiri

# Fungsi untuk menentukan kuadran berdasarkan sudut
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

# Fungsi untuk menentukan jumlah hari berdasarkan nama bulan
def number_of_days(month):
    month = month.lower()  # Ubah input bulan jadi huruf kecil untuk memudahkan pengecekan
    months_31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']  # 31 days
    months_30 = ['april', 'june', 'september', 'november']  # 30 days

    if month in months_31:
        return f"{month.capitalize()} has 31 days."
    elif month in months_30:
        return f"{month.capitalize()} has 30 days."
    elif month == 'february':
        return "February has 28 or 29 days (leap year)."
    else:
        return f"'{month.capitalize()}' is not valid, please enter a correct month name."

# Fungsi untuk menentukan nilai karakter berdasarkan nilai numerik siswa
def letter_grade(score):
    if score >= 90:
        return 'A'  # Jika nilai >= 90
    elif 80 <= score < 90:
        return 'B'  # Jika nilai antara 80 dan 89
    elif 70 <= score < 80:
        return 'C'  # Jika nilai antara 70 dan 79
    elif 60 <= score < 70:
        return 'D'  # Jika nilai antara 60 dan 69
    else:
        return 'F'  # Jika nilai di bawah 60

# Fungsi untuk membaca kode status pernikahan
def marriage_status(code):
    if code.lower() == 'm':
        return "Individual is married."  # Pesan untuk status menikah
    elif code.lower() == 'd':
        return "Individual is divorced."  # Pesan untuk status bercerai
    elif code.lower() == 'w':
        return "Individual is a widower/widow."  # Pesan untuk status duda/janda
    else:
        return "Invalid code entered."  # Pesan untuk kode tidak valid

# Fungsi untuk mengonversi suhu antara Fahrenheit dan Celsius
def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)  # Menggunakan rumus konversi

def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32  # Menggunakan rumus konversi

# Menu utama untuk memilih berbagai fungsi
while True:
    print("Pilihan Program:")
    print("1. Read a character")
    print("2. Determine the quadrant")
    print("3. Number of days in a month")
    print("4. Determine the letter grade")
    print("5. Read marriage status code")
    print("6. Convert temperature")
    print("7. End program")

    # Minta input pilihan dari pengguna
    pilihan = input("Enter your choice (1/2/3/4/5/6/7): ")

    if pilihan == '1':
        # Loop untuk membaca karakter hingga pengguna ingin keluar
        while True:
            char_input = input("Enter a character (or type 'exit' to quit): ")

            if char_input.lower() == 'exit':
                print("Returning to main menu...")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break  # Kembali ke menu utama

            print("The corresponding name is:", get_name_from_char(char_input))
            print('-------------------------------------------------------------')

    elif pilihan == '2':
        # Loop untuk menentukan kuadran hingga pengguna ingin keluar
        while True:
            angle_input = input("Enter an angle in degrees (or type 'exit' to quit): ")

            if angle_input.lower() == 'exit':
                print("Returning to main menu...")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break  # Kembali ke menu utama

            try:
                angle = int(angle_input)
                print(f"The angle {angle} is in {determine_quadrant(angle)}")
                print('-------------------------------------------------------------')

            except ValueError:
                print("Invalid input, please enter a valid number or type 'exit' to quit.")
                print('-------------------------------------------------------------')

    elif pilihan == '3':
        # Loop untuk menentukan jumlah hari hingga pengguna ingin keluar
        while True:
            month_input = input("Enter the name of the month (or type 'exit' to quit): ")

            if month_input.lower() == 'exit':
                print("Returning to main menu...")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break  # Kembali ke menu utama

            print(f"The month {number_of_days(month_input)}")
            print('-------------------------------------------------------------')

    elif pilihan == '4':
        # Loop untuk menentukan nilai karakter hingga pengguna ingin keluar
        while True:
            score_input = input("Enter the student's numerical score (or type 'exit' to quit): ")

            if score_input.lower() == 'exit':
                print("Returning to main menu...")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break  # Kembali ke menu utama

            try:
                score = float(score_input)
                print(f"The letter grade for the score {score} is {letter_grade(score)}")
                print('-------------------------------------------------------------')

            except ValueError:
                print("Invalid input, please enter a valid number or type 'exit' to quit.")
                print('-------------------------------------------------------------')

    elif pilihan == '5':
        # Loop untuk membaca kode status pernikahan hingga pengguna ingin keluar
        while True:
            code_input = input("Enter the marriage status code (M/m, D/d, W/w) or type 'exit' to quit: ")

            if code_input.lower() == 'exit':
                print("Returning to main menu...")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break  # Kembali ke menu utama

            if len(code_input) != 1:
                print("Please enter only one character for the status code.")
                print('-------------------------------------------------------------')
                continue

            print(marriage_status(code_input))
            print('-------------------------------------------------------------')

    elif pilihan == '6':
        # Loop untuk mengonversi suhu hingga pengguna ingin keluar
        while True:
            print("Choices:")
            print("1. Convert from Fahrenheit to Celsius")
            print("2. Convert from Celsius to Fahrenheit")
            print("3. Back to main menu")
            
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                try:
                    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
                    celsius = fahrenheit_to_celsius(fahrenheit_input)
                    print(f"{fahrenheit_input}°F is {celsius:.2f}°C")
                    print('-------------------------------------------------------------')
                except ValueError:
                    print("Invalid input, please enter a valid number.")
                    print('-------------------------------------------------------------')

            elif choice == '2':
                try:
                    celsius_input = float(input("Enter temperature in Celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius_input)
                    print(f"{celsius_input}°C is {fahrenheit:.2f}°F")
                    print('-------------------------------------------------------------')
                except ValueError:
                    print("Invalid input, please enter a valid number.")
                    print('-------------------------------------------------------------')

            elif choice == '3':
                print("Returning to main menu...")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break  # Kembali ke menu utama

            else:
                print("Invalid choice, please choose 1, 2, or 3.")
                print('-------------------------------------------------------------')

    elif pilihan == '7':
        print("Program terminated. Thank You!")
        print('==============================================================')
        break

    else:
        print("Invalid choice, please select 1, 2, 3, 4, 5, 6, or 7.")

