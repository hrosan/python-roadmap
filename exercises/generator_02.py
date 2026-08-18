# IMPORTS
import random as rdm

# FUNCTIONS
def read_pipeline(data: list[float]):
    for value in data:
    # LOOP OVER EACH VALUE INSIDE DATA
        if value > 50.0:
            yield value # Function just yield value above 50

def scale(source, factor: float):
    for i in source:
        yield i * factor

# VARIABLES
rand_list = [round(rdm.uniform(0,100),2) for _ in range(15)]

# CALLING GENERATORS
gen_1 = read_pipeline(rand_list) # Allocating read_pipeline into gen_1
gen_2 = scale(gen_1,2.0)
for i in gen_2:
    print(f"{i:.2f}")