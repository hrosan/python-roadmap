# Importing libraries
import random as rd # importing random librarie to generate random numbers

# Initialize variables
for i in range(10):
    random_number: int = rd.randint(1,100) # random_number allocates a random number from 1 to 100

    # Classifying the random number into categories
    if 1 <= random_number <= 33:
        number_category = "LOW"
    elif 34 <= random_number <= 66:
        number_category = "MID"
    else:
        number_category = "HIGH"

    # Verifying number parity (even/odd)
    if random_number % 2 == 0:
        number_parity = "Even"
    else:
        number_parity = "Odd"

    # Showing the number and its category to user
    print(f"Number {i+1}: {random_number} | Category: {number_category} | Parity: {number_parity}")
    print("---"*30)