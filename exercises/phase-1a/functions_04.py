# IMPORTING LIBRARIES
import random as rdm #Importing random library
from typing import Callable # Python has a built function for a function, because function is not a valid built-in type

# Creating a function
def apply_to_all(numbers: list[float], operation: Callable) -> list[float]:
    '''
        This function works as a HOF, applying a function over a list of numbers
        numbers: a list of float numbers that function will iterate over
        operation: the function will be called inside here    
    '''
     # Looping over the list
    applied_list = [operation(number) for number in numbers] # List comprehension to generate the list
    
    return applied_list # Return the list to the caller 

def square(number: float) -> float:
    return number*number

def invert(number: float) -> float:
    return 1/number if number > 0 else None

# Generating the list
numbers_list = [rdm.uniform(0,10) for _ in range(5)]
for number in numbers_list:
    print(f"{number:.2f}")

# Calling square numbers function
square_numbers = apply_to_all(numbers_list, square)
print("---"*10,"SQUARED NUMBERS","---"*10)
for number in square_numbers:
    print(F"{number:.2f}")

# Calling the invert number function
inverted_numbers = apply_to_all(numbers_list, invert)
print("---"*10,"INVERTED NUMBERS","---"*10)
for number in inverted_numbers:
    if number == 0:
        print(None)
    else:
        print(F"{number:.2f}")