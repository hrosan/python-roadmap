# IMPORTING LIBRARY
from random import uniform

# Creating a list
lst = [uniform(1,20) for _ in range(8)]
# Dictionary comprehesion
dict_test = {f"value_{i}":round(value,2) for i, value in enumerate(lst)} # This a dictionary comprehesion

for key, value in dict_test.items():
    print(f"{key}: {value}")


letters = ["a", "b", "c"]
print(list(enumerate(letters)))