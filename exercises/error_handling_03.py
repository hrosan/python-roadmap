# STARTING A FUNCTION
def parse_sensor_data(data: list[float])->None:
    nbr_lst: list[float] = []
    processed_items: int = 0
    total_valid: int = 0
    total_invalid: int = 0

   # LOOP OVER THE LIST FIRST
    for read in data:
    # HANDLING THE ERROR INSIDE A LOOP
        try: # Here lives the code might crash
            processed_items += 1
            result: float = float(read) # It will rebind read into float - It can crash
        except ValueError: # When the exception occurs, comes here
            print(f"Failed: {read}")
            total_invalid += 1
            continue # Here where the code keep running even if an error occurs
        else:
            total_valid += 1
            nbr_lst.append(result)       
    if nbr_lst:
        lst_avrg = sum(nbr_lst)/len(nbr_lst)
        print(f"Total processed: {processed_items}\nTotal valid: {total_valid}\nTotal Invalid: {total_invalid}\nAverage: {lst_avrg}")
    else:
        print(f"No valid readings - average cannot be calculated")

# CREATE THE DATA
data = ["87.3", "abc", "102.5", "", "56.8", "xyz", "91.2"]
# CALL THE FUNCTION
parse_sensor_data(data)