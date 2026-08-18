# IMPORTS

# FUNCTIONS
def flatten_deep(iterable):
    '''
        THIS FUNCTIONS MUST TAKE ANY ARGUMENT INSIDE AN ITERABLE AND YIELD IT TO USER
    '''
    # LOOP OVER ITERABLE
    for value in iterable:
        # CHECK VALUE TYPE
        if isinstance(value,int): # Check if value is an integer
            yield value # Yield value if true
        elif isinstance(value,list): # Check if value is a list
            yield from value # Yield from iterable if value were a list

# GLOBAL VALUES
data = [1, [2, 3], 4, [5, 6, 7], 8]
gen = flatten_deep(data) # Creating the generator

# ITERATE OVER THE ITERABLE
for value in gen:
    print(value)