# Importing variables
import random as rd

# Initializing a function
def calculate_area(width: float, height: float) -> float:
    return width * height

# Calling the function with different values
for i in range(3):
    print(f"Area: {calculate_area(rd.randint(1,10)*rd.random(),rd.randint(1,5)*rd.random()):.2f} m2")
