# IMPORTS
import random as rdm

# FUNCTIONS | GENERATORS
def generate_readings(count: int, min_val: float, max_val: float):
    '''
        COUNT -> A counter that will tell how many times the loop must execute
        MIN_VAL & MAX_VAL -> Interval that the random float must be in
    '''
    for _ in range(count):
        yield rdm.uniform(min_val,max_val) # send to caller a random value


def filter_outlier(source, low: float, high: float):
    '''
        SOURCE -> Where the input are coming from.
        LOW & HIGH -> Interval accepted where source must be in
        OUTPUT -> Filtered value
    '''
    # USING YIELD FROM
    yield from (value for value in source if low <= value <= high)

def normalize(source, min_val: float, max_val: float):
    '''
    NORMALIZE READING COMING FROM OUTSIDE SOURCE
    SOURCE -> Where the data is coming from
    MIN_VAL & MAX_VAL -> Interval where data must be normalized
    OUTPUT -> A normalized value
    '''
    # NORMALIZING VALUES
    for value in source: # Take every value coming from outside
        # NORMALIZE DATA | 0.0 - 1.0
        normalize_value = (value - min_val)/(max_val - min_val) # Normalize
        yield round(normalize_value,2)

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
        yield chunk_list # At the end send the remain number

# TESTING FUNCTIONS
readings = generate_readings(20,0,100) # Calling the generator | 20 readings in the interval [0,100]
filtered_readings = filter_outlier(readings,10,90) # Generator filters readings in the interval [10,90] | 80% of readings
normalized_readings = normalize(filtered_readings,10,90) # Normalize each value
chunked_list = chunk(normalized_readings,3) # Chunking in list of 3 elements

# FILTERING VERIFICATION
for value in chunked_list:
    print(f"Chunked list: {value}")