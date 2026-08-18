# IMPORTS

# FUNCTIONS
def count_up(limit: int):
    count = 0
    while count <= limit:
        yield count
        count += 1

# TESTING FUNCTION
gen = count_up(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

