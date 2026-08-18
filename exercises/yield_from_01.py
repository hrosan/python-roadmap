# IMPORTS

# FUNCTIONS
def flatten(nested: list[list]):
    for inner_list in nested:
        yield from inner_list # It will yield every item inside the inner list

# GLOBAL VARIABLES
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

gen_number = flatten(nested)

for item in gen_number:
    print(item)