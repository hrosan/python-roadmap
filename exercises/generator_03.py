# IMPORTS
import random as rdm

# FUNCTIONS
def running_average(source: float):
    # INITIALIZE LOCAL VARIABLES
    count = 0
    total = 0
    for value in source:
        total += value # Accumulate each value into total
        count += 1 # Increment counter
        yield round(total/count,2)

# GLOBAL VARIABLE
numbers = [rdm.uniform(1,100) for _ in range(15)]
gen = running_average(numbers)
# LOOP OVER THE GENERATOR | USING ENUMERATE
for i, avg in enumerate(gen,start=1):
    print(f"After {i} values: {avg:.2f}") # I don't need to use next because gen is an iterator
