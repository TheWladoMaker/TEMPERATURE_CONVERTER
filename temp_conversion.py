# Importing required library
import time

# Defining function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Celsius = (Fahrenheit - 32) * 5/9
    celsius = ((fahrenheit - 32) * 5) / 9
    return celsius

# Defining function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Fahrenheit = Celsius * 9/5 + 32
    fahrenheit = ((celsius * 9) / 5) + 32
    return fahrenheit

# Function to simulate loading or processing time
def points():
    points = ['.','.','.','.','.']
    for point in points:
        time.sleep(0.5)
        print(point, end = " ")

# Starting program
print('''Welcome to this program. This program will help you to transform temperatures from Celsius to Fahrenheit and vice versa.''')

# Loop to keep program running
while True:
    # Nested loop to handle user input
    while True:
        chose_which = input("\nWhat type of data do you want to convert: Celsius or Fahrenheit? ")

        # User chooses to convert Fahrenheit to Celsius
        if 'fahrenheit' in chose_which.lower():
            print('\nYou have chosen Fahrenheit to Celsius.')
            points()
            fahrenheit = int(input('\nPlease enter the Fahrenheit value you want to convert: '))
            points()
            print(f'\nYou entered the value of {fahrenheit} °F, this value converted in Celsius is: {fahrenheit_to_celsius(fahrenheit)}')
            break  # Exit loop

        # User chooses to convert Celsius to Fahrenheit
        elif 'celsius' in chose_which.lower():
            print('\nYou have chosen Celsius to Fahrenheit.')
            points()
            celsius = int(input('\nPlease enter the Celsius value you want to convert: '))
            points()
            print(f'\nYou entered the value of {celsius} °C, this value converted in Fahrenheit is: {celsius_to_fahrenheit(celsius)}')
            break  # Exit loop

        else:
            print("\nInvalid input! please enter a valid request.\n")

    # Ask user if they want to convert another data point
    chose_y_n = input("\nWould you like to convert another data point? Yes or no?: ")
    points()
    if 'yes' in chose_y_n.lower():
        pass

    elif 'no' in chose_y_n.lower():
        break  # Exit loop

print("\nThanks to use this program, you are welcome to comeback again any time you want")
