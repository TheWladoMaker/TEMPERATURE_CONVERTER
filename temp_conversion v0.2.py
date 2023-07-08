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
    points = ['.', '.', '.', '.', '.']
    for point in points:
        time.sleep(0.5)
        print(point, end=" ")


# Starting program
print(
    '''Welcome to this program. This program will help you to transform a set of temperatures from Celsius to Fahrenheit and vice versa.''')


# Nested loop to handle user input
while True:
    while True:
        chose_which = input("\nWhat type of data do you want to convert: Celsius or Fahrenheit? ")
        if chose_which.lower() not in ['celsius', 'fahrenheit']:
            print("\nInvalid input! please enter a valid request.\n")

        else:
            break

    # User chooses to convert Fahrenheit to Celsius
    if 'fahrenheit' in chose_which.lower():
        print('\nYou have chosen Fahrenheit to Celsius.')
        points()

        # Loop to handle user input
        while True:
            try:
                fahrenheit_temp_list = input('\nPlease enter the Fahrenheit value or values you want to convert (separated by spaces): ')
                fahrenheit_temp_list = list(map(float, fahrenheit_temp_list.split()))

                # Calling function to convert Fahrenheit to Celsius
                points() 
                for temp in fahrenheit_temp_list:
                    print(
                        f'\nYou entered the value of {temp} °F, this value converted in Celsius is: '
                        f'{round(fahrenheit_to_celsius(temp),2)}')
                    time.sleep(0.5) # Simulate loading time
                break  # Exit loop
            except ValueError:
                print("\nInvalid input! please enter a valid request.\n")

    # User chooses to convert Celsius to Fahrenheit
    elif 'celsius' in chose_which.lower():
        print('\nYou have chosen Celsius to Fahrenheit.')
        points()
        while True:
            try:
                celsius_temp_list = input('\nPlease enter the Celsius value or values you want to convert (separated by spaces): ')
                celsius_temp_list = list(map(float, celsius_temp_list.split()))

                # Calling function to convert Celsius to Fahrenheit
                points()
                for temp in celsius_temp_list:
                    print(
                        f'\nYou entered the value of {temp} °C, this values converted in Fahrenheit is: '
                        f'{round(celsius_to_fahrenheit(temp),2)}')
                    time.sleep(0.5) # Simulate loading time
                break  # Exit loop
            except ValueError:
                print("\nInvalid input! please enter a valid request.\n")
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
