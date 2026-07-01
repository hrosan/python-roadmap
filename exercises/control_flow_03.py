# Importing Libraries
import random as rd

# Initializing variables
counter: int = 0
random_number: int = 0

# Loop
while True:
    random_number = rd.randint(1,100) # Generate a random number
    if random_number % 7 == 0 and random_number > 50:
        break # If the requirements were met break the loop
    print(f"Number Generated: {random_number}") # Print the number generated
    counter += 1 # raise by 1 counter value

# Showing the result
print(f"Found: {random_number} | Attempts: {counter}")
