# IMPORTS
import random as rdm
# FUNCTIONS
def chunk(source,size):
    # IT MUST RETURN A CHUNK ITERABLE
    chunk_list = []
    for item in source:
        chunk_list.append(item)
        if len(chunk_list) == size:
            yield chunk_list # Send to caller
            # IN THE NEXT CALL IT WILL START FROM HERE
            chunk_list = [] # This part execute after next() call
    # LAST CALL AFTER END SOURCE LOOP
    if chunk_list: # If chunk list not empty
        yield chunk_list # At the end send the remain numbers

# TESTING
random_list = [round(rdm.uniform(1,10),2) for _ in range(14)] # Generate a list of floats
gen = (chunk(random_list,5))
for part in gen:
    print(part)