# DATA
readings = [
    {"sensor": "T-01", "value": 87.3},
    {"sensor": "T-02", "value": 34.1},
    {"sensor": "T-03", "value": 102.5},
    {"sensor": "T-04", "value": 56.8},
    {"sensor": "T-05", "value": 91.2},
]

# APPLY LAMBDA FUNCTIONS
filter_list: list[dict[str,float]] = list(filter(lambda r: r["value"]> 80, readings)) # Filtering values above 80
print(f"FILTERED LIST: {filter_list}")
values_list: list[float] = list(map(lambda v: v["value"], filter_list)) # Extracting just the values from the list
print(f"VALUES LIST: {values_list}")
readings.sort(key=lambda r: r["value"],reverse= True) # Sorting reading by value in descending mode
print(f"READING SORTED: {readings}")
