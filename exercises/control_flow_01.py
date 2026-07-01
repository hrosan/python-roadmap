# Importing libraries
import random as rd # importing random librarie to generate random numbers

# Initialize variables
random_number: int = rd.randint(1,100) # random_number allocates a random number from 1 to 100


# Classifying the random number into categories
if 1 <= random_number <= 33:
    number_category = "LOW"
elif 34 <= random_number <= 66:
    number_category = "MID"
else:
    number_category = "HIGH"

# Showing the number and its category to user
print(f"Number: {random_number} | Category: {number_category}")