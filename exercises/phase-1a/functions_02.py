# Importing Librarie
import random as rd

# Stating a function
def classify_temperature(temp: float) -> str:
    if temp < 15:
        return "Cold"
    elif 15 <= temp < 25:
        return "Warm"
    else:
        return "Hot"


# Printing the status
for i in range(5):
    random_temp = rd.uniform(-5,40) # Generating random temperature using random.uniform
    print(f"Temp: {random_temp:.2f}")
    print(f"Status: {classify_temperature(random_temp)}")