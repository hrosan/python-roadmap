# IMPORTING LIBRARY
from random import uniform

# CREATE THE INITIAL VARIABLES
lst_dicts: list[dict[str,list[float]]] = []
sensor_reading: dict[str,list[float]] = {}
# CREATING A BUNCH OF DICTIONARIES AD POPULATING IT
for i in range(8):
    sensor_reading = {
        'sensor': f"T-0{i}",
        'value': [round(uniform(50,100),2) for _ in range(5)]
    }
    # ADDING A DICTIONARY INTO A LIST
    lst_dicts.append(sensor_reading.copy()) # Appending the dictionary copy into a list

for readings in lst_dicts:
    values: list[float] = readings['value'] # Just allocate readings list into a variable
    average: float = round(sum(values)/len(values),2) # Calculates the average from readings
    print(f"Sensor: {readings['sensor']} | Average: {average}")