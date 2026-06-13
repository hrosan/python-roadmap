# INITIALIZING VARIABLES
user_name: str = input("Write your name: ") # The user should write his/her name
user_age: int = int(input("What's you age: ")) # The user should write his/her age. The int function will do th type casting

future_age: int = user_age + 5 # Giving the age five years in the future

# SHOWING THE INFORMATIONS
print(f"Hello my name is {user_name}, I have {user_age} yrs") # Showing the information to the user
print(f"In five years I'll be {future_age} old")