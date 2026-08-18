# IMPORTS
import random as rdm

# FUNCTIONS
def positive_numbers(numbers: list[int]):
    yield from numbers

def negative_numbers(numbers: list[int]):
    yield from numbers

def all_numbers(source_1 , source_2):
    yield from source_1
    yield from source_2

# GLOBAL VARIABLES
pos_numbers = sorted([rdm.randint(1,10) for _ in range(7)], reverse= True)
neg_numbers = sorted([-rdm.randint(1,10) for _ in range(7)], reverse= True)


# CALLING FUNCTIONS
gen_pos = positive_numbers(pos_numbers)
gen_neg = negative_numbers(neg_numbers)

both_numbers = all_numbers(gen_pos,gen_neg)

# LOOP OF GENERATOR
for numbers in both_numbers:
    print(numbers)