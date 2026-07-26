# LIBRARY IMPORT
from random import uniform # Importing just uniform function
from typing import Callable # Importing just Callable function

# CREATING FUNCTION 
def summarize_stats(*args: float, **kwargs: dict) -> None:
    key, value = kwargs.items() # Getting the key and value from the kwargs items



# CREATING THE DATASET
# Creating the lists
a = uniform(1,15)
b = a**(uniform(2,5))
c = b/(uniform(2/10))
d = a*c
e = (d**a)/(c-b)
# Creating the dictionaries
first_dict: dict[str,str] = {"label": "Scores dataset"}