# Importing Libraries
import random as rd

list_numbers: list[int] = [rd.randint(1,100) for i in range(20)] # Generate a list of 20 numbers by random

# Looping through the list
for number in list_numbers:
    if number < 20:
        continue # Start with another number if requirement is met
    if number > 90:
        print(f"Stopped at: {number}")
        break # Go out from loop if number is greater than 90

    print(f"Number: {number} | Square: {number**2}")


even_numbers= [x*2 for x in list_numbers if x%2==0]
print(even_numbers)