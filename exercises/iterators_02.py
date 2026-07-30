# IMPORT LIBRARY

# FUNCTIONS
def manual_enumerate(iterable) -> list[tuple[int,str]]:
    # INNER VARIABLES
    counter: int = 0 # Counter for enumerate each iteration
    it = iter(iterable) # It allocates the iterable
    it_lst: list[tuple] = []
    # LOOP OVER ITERABLE
    while True:
        try:
            aux_tuple = (counter,next(it)) # Passing next(it) because this statement shows the real value
            it_lst.append(aux_tuple) # appendin' the tuple inside a list
            counter += 1 # Increment counter
        except StopIteration:
            break # End while loop
    return it_lst

# CALLING THE FUNCTION
test = manual_enumerate(["a", "b", "c", "d"])
print(test)