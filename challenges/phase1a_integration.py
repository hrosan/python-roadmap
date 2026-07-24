# LIBRARIES
import random as rdm # Importing random library - Use uniform()
# GLOBAL VARIABLES
sensor_reading: list[dict] = []
sensor:dict = {}
sensor_set: tuple[str] = ("T-01","T-02","T-03","T-04","T-05")
# DATA GENERATION
    # CREATING THE LIST OF DICTIONARIES
for i in range(20):
    # GENERATE DICTIONARIES WITH RANDOM VALUES
    sensor["ID"] = rdm.choice(sensor_set) # Take by random one element from the tuple sensor_set
    sensor["value"] = rdm.uniform(-10,150) # Generate a random read value for the sensor
    sensor["unit"] = "celsius"
    # ADD THE DICTIONARIES INTO A LIST
    sensor_reading.append(sensor.copy()) # Append a shallow copy to the list

# PARSING FUNCTION
def parse_reading(**sensor_data: dict)->float:
    # VALIDATE VALUE TYPE
    value = sensor_data.get("value") # Get the value coming from a dictionary, if there's not keep it silent
    if not isinstance(value,(int,float)):
        raise TypeError (f"Value data type doesn't match with valid type (Number)")
    # VALIDATE VALUE RANGE
    if value < -10 or value > 140:
        raise ValueError (f"Value is out of range!")
    # RETURN TO USER
    return round(value,2)

# FUNCTION TO RUN A PIPE-LINE
def run_pipeline(*readings, threshold=100,label = 'Celsius Monitor') -> dict:
    '''
    This function takes two arguments
    *readings - arguments of reading dictionary
    **config - basic configurations for dictionary implementing:
        threshold [float] -> default 100.0
        label [str] -> "Pipeline"
    This function returns a dictionary to caller
    '''
    error_readings: int = 0
    valid_readings = []
    # LOOP OVER READINGS
    for data in readings:
        # PROCESSING DATA AND HANDLING ERRORS
        try:
            parsed_data = parse_reading(data) # Take the result coming from parse reading
            valid_readings.append(parsed_data)
            data_read += 1
        except ValueError as value:
            # COUNT ERRORS
            error_readings += 1
            continue # Returning to loop
        except TypeError as t_error:
            # COUNT ERROR
            error_readings += 1
            continue # Returning to loop

