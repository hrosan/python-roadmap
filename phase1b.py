class Subscriber:
    def __init__(self, username: str):
        self.username: str = username
        self.watchlist: list[str] = [] # Initial list collection
        self.history: dict = {} # Initial dictionary collection

    # INITIALIZING A METHOD (Behavior)
    def add_to_watchlist(self, movie: str):
        if movie not in self.watchlist:
            self.watchlist.append(movie)
            print(f"Movie {movie} was added to {self.username}'s watchlist!")
        else:
            print(f"{movie} is already in your watchlist!")

# INSTANTIATING A NEW SUBSCRIBER
new_subscriber = Subscriber("developer_one")
print(new_subscriber) # It will output a memory address allocation
print(new_subscriber.username) # It will output the developer username

platform_user = {} # Initializing a dictionary
platform_user["developer"] = new_subscriber # Now the information is stored into a dictionary
print(platform_user["developer"]) # It will output a memory allocation address, because a dictionary is an information container
print(platform_user["developer"].username) # It will output the developer username

'''
# Adding movies to the watchlist # THIS METHOD IS WRONG
platform_user["movielist"] = new_subscriber.watchlist.append("Matrix")
print(platform_user["movielist"].watchlist)
'''

# WRONG WAY - WHEN HANDLING CLASSES
new_subscriber.watchlist.append("Matrix")
print(new_subscriber.watchlist)

# Using a METHOD to add a new movie
new_subscriber.add_to_watchlist("Inception") # Adding the movie to the watchlist using a class-method 

# Adding the movie into the dictionary
platform_user["developer"].add_to_watchlist("Interstellar") # Adding a movie using a dictionary statement
print(platform_user["developer"].watchlist) # Verifying every item inside the watchlist

# LIST COMPREHESIONS
uppercase_movies = [movie.upper() for movie in platform_user['developer'].watchlist]
print(uppercase_movies)

