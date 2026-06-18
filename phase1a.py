# IMPORTING LIBRARIES
from random import randint # From random the function randint has been imported to generate random numbers

# FUNCTIONS
def check_age(age: int = 0):
    if age < 0:
        raise ValueError
    # It start verifying from top to bottom ages.
    if age >= 18: # Verify if the user age is greater or equal to 18
        print("You're considered an adult!") # Show a message if the condition above is true
    elif age >= 13: # If the condition above in't true, it will look here. Verifies if the user age is between 13 and 18
        print("You're considered a teenager!") # If the condition above is true, show a message to the user
    else: # Finally, if both of conditions haven't been satisfied will enter here
        print("You're a child, don't worry you will grow up soon Kiddo!") # If the condition above is true, show the message to the user


# Generating random ages using "for" + range((randint()))
for i in range(randint(1,10)): 
    # INITIALIZING VARIABLES
    # user_name: str = input("Write your name: ") # The user should write his/her name
    user_age: int = randint(5, 100) # I'm using the function randint(a,b) that generates integer number between 'a' and 'b'
    # future_age: int = user_age + 5 # Giving the age five years in the future
    print(f"USER: {i} | AGE: {user_age}")
    # Using the function
    check_age(user_age)
    

'''
# SHOWING THE INFORMATIONS
print(f"Hello my name is {user_name}, I have {user_age} yrs") # Showing the information to the user
print(f"In five years I'll be {future_age} years old") #
'''