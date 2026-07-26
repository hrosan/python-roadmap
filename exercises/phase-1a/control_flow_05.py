# Importing libraries
import random as rd

# Initializing variables
random_numbers: list[int] = [rd.randint(1,100) for _ in range(15)] # Generates a list with 15 random numbers
print(random_numbers)
low_counter: int = 0 # A counter for low values range
mid_counter: int = 0 # A counter for mid values range
high_counter: int = 0 # A counter for high values range


# Lopping over the list
for number in random_numbers:
    if number < 34:
        low_counter += 1 # Increment low counter
    elif number == 50:
        continue
    elif 34 <= number <= 66:
        mid_counter += 1 # Increment mid counter
    else:
        high_counter += 1 # Increment high counter

# Showing the information to user
print(f"Low: {low_counter} | Mid: {mid_counter} | High: {high_counter}")