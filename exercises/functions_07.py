


# CREATING A FUNCTION
def summarize_stats(*args: float, **kwargs) -> None:
    # INITIALIZING DEFAULT VALUES TO KWARGS
    data_label = kwargs.get("label", "Dataset") # Search for 'Label' in Kwargs, if there isn't create the pattern 'Dataset'
    data_decimals = kwargs.get("decimals", 2) # Search for 'decimals' in kwargs, if there isn't any create the pattern 2

    # CALCULATING EACH VALUE ROUNDING THE DECIMAL PLACES
    min_args = round(min(args), data_decimals) # Get the minimum value coming from args
    max_args = round(max(args),data_decimals) # Get the max value coming from args
    mean_args = round((sum(args)/len(args)),data_decimals) # Calculate the mean using args
    
    # OUTPUT
    print(f"{data_label}:\nMin: {min_args:.{data_decimals}f} | Max: {max_args:.{data_decimals}f} | Mean: {mean_args:.{data_decimals}f}")
    




# FUNCTION CALLING TEST
summarize_stats(10.5, 23.1, 8.7)
summarize_stats(10.5, 23.1, 8.7, 45.2, 67.8, label="Sensor Readings")
summarize_stats(10.5, 23.1, 8.7, 45.2, 67.8, 12.3, 98.1, 33.4,label="Pressure Log", decimals=4)