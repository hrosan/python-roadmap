# Designing the blueprint
class UserBlueprint: # Designing the blueprint
    # __init__ -> runs automatically the moment a new object is built.
    def __init__(self, owner_name: str): 
        # self -> The object's ay of referring to itself and holding onto its own data
        pass # Just means "Leave this empty for now"

class Subscriber:
    def __init__(self, user_name: str):
        self.username: str = user_name # It comes from the parameter
        self.watchlist: list[str] = [] # List for every movie the user have already watched

    # Creating a method to add the movie into the user list
    def add_to_watchlist(self, movie_name, is_active: bool) -> None:
        # Adding a movie into the watchlist
        self.watchlist.append(movie_name)
        self.is_active = is_active
        print(f"The movie {movie_name} has been added successfully")

# Creating new users
user_one = Subscriber("Henrique", True) # It creates a new person called Henrique
user_two = Subscriber("Mariana", False)

# Creating an empty dictionary to act as a database
platform_users = {} # Those brackets act like an empty dictionary

# Adding the users inside the dictionary
platform_users['Devone'] = user_one # dictionary[key] = value -> platform_user['Devone'] = user_one
platform_users['Devtwo'] = user_two

# Adding movies to users' watchlist
platform_users['Devone'].add_to_watchlist("Matrix") # Adding the movie Matrix inside the user_one's list
platform_users['Devtwo'].add_to_watchlist("Pulp Fiction")
platform_users['Devone'].add_to_watchlist("Interstellar")
print(f"User name: {platform_users['Devone'].username} | User movie list: {platform_users['Devone'].watchlist}")

print(platform_users['Devone'].values)