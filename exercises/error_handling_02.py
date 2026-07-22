# CREATE A FUNCTION
def read_sensor(readings: list[float], index: int) -> float:
# VALIDATE PARAMETERS BEFORE OPERATING
    try:
        if not isinstance(index,int):
            raise TypeError(f"Your index type doesn't match the specified type {type(index).__name__}")
        if index > len(readings)-1:
            raise IndexError(f"Your index value isn't valid")
        # ACCESS READINGS VALUE BY INDEX
        value_reading = readings[index] # Acessing and getting the value coming from readings list
        if value_reading == 0:
            raise ZeroDivisionError(f"Zero division at the index")        
# EXCEPT-FINALLY BLOCK
    except IndexError as e:
        print(f"Index error: {index}")
    except ZeroDivisionError as e:
        print(f"Zero division error: {e}")
    except TypeError as e:
        print(f"Type error: {e}")
    else:
        # RETURN VALUE TO CALLER
        print("Operation result is a success!")
        return 100/value_reading
    finally:
        print("Read attempt complete!")

read_sensor([10.0, 0.0, 5.0], 0)   
read_sensor([10.0, 0.0, 5.0], 1)   
read_sensor([10.0, 0.0, 5.0], 10)  
read_sensor([10.0, 0.0, 5.0], "1")