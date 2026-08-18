# IMPORTS

# FUNCTIONS
def pipeline(sources: list[list[float]]):
    counter = 0
    for source in sources:
        counter += 1
        yield f"--- Processing Source {counter} ---"
        yield from normalize(source,max(source),min(source)) # Yield into a normalize function

def normalize(sources: list, max_value: float, min_value: float):
    for value in sources:
    # TAKING EACH VALUE
        normalizing = (value - min_value)/(max_value - min_value)
        yield round(normalizing,2)

# TESTING
sources = [
    [10.0, 20.0, 30.0, 40.0, 50.0],
    [100.0, 200.0, 300.0],
    [5.0, 15.0, 25.0, 35.0]
]

gen = pipeline(sources)

for value in gen:
    print(value)