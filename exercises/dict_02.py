'''
Build a dictionary where:
- Key is the sensor name
- Value is a list of all readings for that sensor

Then print each sensor and its average reading 
rounded to 2 decimal places.
'''

readings = [
    {"sensor": "T-01", "value": 87.3},
    {"sensor": "T-02", "value": 102.1},
    {"sensor": "T-01", "value": 91.5},
    {"sensor": "T-03", "value": 78.4},
    {"sensor": "T-02", "value": 95.0},
    {"sensor": "T-01", "value": 88.7},
]

group_dict: dict[str,list[float]] = {}

# LOOPING OVER THE LIST
for read in readings:
    # GETTING THE VALUES FROM EACH KEY
    sensor: str = read.get('sensor') # Getting the sensor name and allocating into the variable
    value: float = read.get('value') # Getting the valor and allocating it into the variable

    '''
    # VERIFYING THE EXISTENCE OF SENSOR
    if sensor not in group_dict:
        group_dict[sensor] = [] # Create a new key-value pair if Sensor doesn't exist inside the dictionary
    
    # APPENDING THE VALUE INTO THE LIST
    group_dict[sensor].append(round(value,2))
    '''
    group_dict.setdefault(sensor,[]).append(value)

# PRESENTING THE DICT TO THE USER
for key, value in group_dict.items():
    print(f"{key} | Average: {round((sum(value)/len(value)),2)}")