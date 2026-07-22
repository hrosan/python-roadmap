# Importing libraries
from random import uniform

# Initializing a function
def summarize(sum_list: list[float]) -> dict[str, float]:
    sum_dict = {}
    # Creating the dictionary
    sum_dict["min"] = min(sum_list) # min() gets smallest value from a list
    sum_dict["max"] = max(sum_list) # max() gets the highest value from a lits
    sum_dict["mean"] = sum(sum_list)/len(sum_list) # mean() calculates the arithmetic average
    sum_dict["range"] = sum_dict["max"] - sum_dict["min"]

    return sum_dict # returns the dictionary

# Initializing variables
dict_sum: dict = {}

# Creating a list of float numbers
test_list = [uniform(1.00,100.00) for _ in range(10)]

# Put the list inside the function
dict_sum = summarize(test_list)

# Printing the output
for key,value in dict_sum.items():
    print(f"{key}: {value:.2f}")