# IMPORTS
import random as rdm # Importing random library
import string # importing string library

# VARIABLE | GENERATE RANDOM LISTS
range_a = rdm.randint(1,10)
a = [rdm.choice(string.ascii_letters) for _ in range(range_a)] # Create a random length list with random ascii letters | Whole alphabet uppercase and lowercase
range_b = rdm.randint(1,10)
b = [rdm.choice(string.digits) for _ in range(range_b)] # Create a random length list with random digits | From 0 to 9

# FUNCTION
def zip_two(iterable_1, iterable_2) -> list[tuple]:
    # LOCAL VARIABLES
    zip_list: list[tuple] = []
    it_1 = iter(iterable_1)
    it_2 = iter(iterable_2)
    # LOOP OVER ITERABLES
    while True:
        # ERROR HANDLING
        try:
            # MAKE THE ZIP BETWEEN ITERABLES
                zip_pair: tuple = (next(it_1),next(it_2)) # Allocating both iterables in a tuple
                zip_list.append(zip_pair) # Put the paired tuple into a list
        except StopIteration:
            # WHEN GET ITERATION
            break # Leave the loop
    # AFTER ENDING
    return zip_list

# CALLING A FUNCTION
test = zip_two(a,b)
for x in test:
     print(f"{x}")
