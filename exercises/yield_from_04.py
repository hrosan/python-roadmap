# IMPORTS

# FUNCTIONS
def read_chunk(source: list[list]):
    # ITERATE OVER THE OTTER LIST
    counter = 0
    for element in source:
        # FIRST TAKE THE INNER LIST
        counter += 1 # It will warn about inner list index
        # YIELD DE COUNTER VALUE TO CALLER
        yield f"--- Source {counter} ---" 
        yield from element # Using yield from to yield over inner list


# TEST FUNCTION
sources = [
    [10, 20, 30],
    [40, 50],
    [60, 70, 80, 90]
]
gen = read_chunk(sources)

# ITERATE OVER GENERATOR
for element in gen:
    print(element)
