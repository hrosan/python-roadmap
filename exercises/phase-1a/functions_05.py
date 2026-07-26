# IMPORTING LIBRARIES
import random as rdm
from typing import Callable

# CREATING THE CLOSURING FUNCTION
def make_validator(threshold: float) -> Callable:
    def validate_threshold(value: float) -> bool:
        return value > threshold # It will return True/False
    return validate_threshold

# CREATING A LIST OF FLOAts
validate_value: list[float] = [rdm.uniform(0,150) for i in range(10)]

# CREATING THE VALIDATORS
is_hot = make_validator(25.0) # This is the first threshold to verify
is_high_pressure = make_validator(100.0) # This is the second threshold to verify

# Looping over the list and verifying each value, also printing each output
for value in validate_value:
    print(f"Value: {value:.2f} | Hot: {is_hot(value)} | High Pressure: {is_high_pressure(value)}")
