# IMPORTS

# VARIABLES
string_lst: list[str] = ["alpha","beta","gama","delta","epsilon"]

# ITER TO ITERATE OVER THE LIST
it = iter(string_lst) # Putting the string in a iterator

# USE NEXT
print(next(it)) # alpha
print(next(it)) # beta
print(next(it)) # gama
print(next(it)) # delta
print(next(it)) # epsilon - iter exhausted here
# HANDLING ERROR
try:
    # CALLING NEXT ONE MORE TIME
    print(next(it)) # It will generate an error StopIteration
except StopIteration:
    print("Iterator exhausted") # Warn user that there's no more iterators